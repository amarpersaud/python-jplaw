"""
Requestor allows HTTP communication.
"""
from enum import Enum
import requests
import json
from typing import Dict, Any, TypeVar
from jplaw.api_paths import *
from jplaw.types.http_type import HttpType

T = TypeVar("T")

class Requestor:
    def __init__(self, instance:str, username:str, password:str, headers: Dict[str, str]):
        """
        Make an HTTP requestor
        
        Args:
            instance (str): URL of instance to log in to or use
            username (str): username or email to log in with
            password (str): password of user
            headers (Dict[str,str]): Header data
        Returns:
            Requestor object
        """
        self.headers = headers
        self.instance = instance
        self.auth_token = None
        if(username and password):
            self.auth_token = self.login(username=username, password=password, instance=instance)
            
    def request(self, type_: HttpType, url: str, form: Dict[str, Any]) -> T:
        """
        Make an HTTP request
        
        Args:
            type_ (HttpType): Type of request
            url (str): full url of endpoint
            form (Dict[str,Any]): dictionary with data to send
        Returns:
            json object of response
        """
        if type_ == HttpType.GET:
            response = requests.get(url, params=form, headers=self.headers)
        else:
            headers = {
                "Content-Type": "application/json",
                **self.headers,
            }
            response = requests.request(type_.value, url, data=json.dumps(form), headers=headers)
        if response.status_code != 200:
            raise Exception(response.text)  # Adjust this according to how your API returns errors
        
        return response.json()
    
    def apiURL(self, path:str, instance:str=None):
        """
        Converts API path to full API URL
        
        Args:
            path (str): Path in api (minus version number), starting with "/"
            instance (str): instance to access. Default None uses logged in instance
        Returns:
            URL of api endpoint
        """
        url = instance or self.instance
        return url.rstrip("/") + API_VERSION.rstrip("/") + path
    
    def lemmyRequest(self, function: str, instance: str = None, form: Dict[str, Any]={}, optional: Dict[str, Any]={}, auth:bool=True) -> T:
        """
        Make an api request specifically to a lemmy instance for a given api function
        
        Args:
            type_ (HttpType): Type of request
            function (str): API function
            instance (str): instance to access. Default None uses logged in/default instance
            form (Dict[str,Any]): dictionary with data to send
            auth (bool): Whether or not to authenticate. Will use internal auth_token from login if available, otherwise doesn't authenticate
            
        Returns:
            request response
        """
        form = self.AddListIfValue(optional=optional, form=form)
        form = self.fixFormValues(form)
        
        #Only authorize if authorization enabled, token is available, and instance is not changed. If instance changed or logged out, disable auth. 
        if(auth and (self.auth_token is not None) and ((instance is None) or (instance == self.instance))):
            form["auth"] = self.auth_token
        return self.request((API_PATH[function]["method"]), self.apiURL(instance=instance, path=(API_PATH[function]["path"])), form)
    
    def logout(self):
        """
        Logs out of instance
        """
        #TODO: send log out 
        self.auth_token = None
    
    def login(self, username, password, instance=None):
        """
        Log into instance
        Args:
            username: username or email in instance
            password: password for login
            instance (str): instance to access. Default None uses logged in/default/constructor instance
        Returns:
            Access token
        """
        self.instance = instance or self.instance
        form = { "username_or_email": username, "password": password }
        res_data = self.lemmyRequest("login", form=form, instance=instance, auth=False)
        return res_data["jwt"]
    
    def boolToStr(self, bool_val:bool):
        """
        Convert a boolean value to a lowercase string for request
        
        Args:
            bool_val (bool): boolean value to convert to string
        
        Returns:
            "true" if True, "false" if false, "none" if None.
        """
        if(bool_val is None):
            return "none"
        return str(bool_val).lower() if isinstance(bool_val, bool) else bool_val
        
    def fixFormValues(self, form: Dict[str, Any]):
        """
        Fix value types for requests (e.g. Enum types)
        
        Args:
            form (Dict[str, Any]): Dictionary of keys and items in form
        
        Returns:
            Form with fixed values
        """
        for key, value in form.items():
            if(isinstance(value, Enum)):
                form[key] = value.value
        return form
    
    def AddIfValue(self, name:str, value: Any, form: Dict[str, Any]):
        """
        Adds items to form if not None
        Args:
            name (str): Key of item to add
            value (Any): Value of item to add to form
            form (Dict[str, Any]): Dictionary to add optional arguments to if not none.
        Returns:
            Form with optional item.
        """
        if(value is not None):
            form[name]=value
        return form
    
    def AddListIfValue(self, optional: Dict[str, Any], form: Dict[str, Any]):
        """
        Adds items from optional list to form if not None
        Args:
            optional (Dict[str, Any]): Dictionary of options with string keys and value.
            form (Dict[str, Any]): Dictionary to add optional arguments to if not none.
        Returns:
            Form with optional items.
        """
        if(optional is not None):
            for key in optional:
                if(optional[key] is not None):
                    form[key]=optional[key]
        return form
