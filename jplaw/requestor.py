from enum import Enum
import requests
import json
from typing import Dict, Any, TypeVar
from .api_paths import *
from .http_type import HttpType

T = TypeVar("T")

class Requestor:
    def __init__(self, instance:str, username:str, password:str, headers: Dict[str, str]):
        """
        Make an HTTP request
        
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
    
    def lemmyRequest(self, function: str, instance: str = None, form: Dict[str, Any]={}, optional: Dict[str, Any]={}, auth:bool=True, auth_token:str=None) -> T:
        """
        Make an api request specifically to a lemmy instance for a given api function
        
        Args:
            type_ (HttpType): Type of request
            function (str): API function
            instance (str): instance to access. Default None uses logged in/default instance
            form (Dict[str,Any]): dictionary with data to send
            auth (bool): Whether or not to authenticate. Will use auth_token if available first, then internal auth_token from login.
            auth_token (str): authentication token
        Returns:
            request response
        """
        form = self.AddListIfValue(optional=optional, form=form)
        
        #if auth and token available 
        if(auth and (auth_token or self.auth_token)):
            form["auth"] = auth_token or self.auth_token
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
        res_data = self.lemmyRequest("login", form=form, instance=instance)
        return res_data["jwt"]
    
    def AddIfValue(self, name, value, form):
        """
        Adds items to form if not None
        Args:
        
        Returns:
            Access token
        """
        if(value is not None):
            form[name]=value
        return form
    
    def AddListIfValue(self, optional: Dict[str, Any], form: Dict[str, Any]):
        if(optional is not None):
            for key in optional:
                if(optional[key] is not None):
                    form[key]=optional[key]
        return form
