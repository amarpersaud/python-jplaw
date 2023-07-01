"""
Emoji class. Designed to allow Lemmy.Emoji functions.
"""
from jplaw.requestor import Requestor
from jplaw.api_paths import *
from typing import List
from jplaw.types.modlog_action_type import ModlogActionType
from jplaw.types.listing_type import ListingType
from jplaw.types.registration_mode import RegistrationMode

class Emoji():
    def __init__(self, _req: Requestor):
        self._req = _req
    
    def create(self, category:str, shortcode:str, image_url:str, alt_text:str, keywords:List[str], instance:str=None, auth_token:str=None):
        """
        Create a custom emoji
        
        Args:
            category (str): Category of the emoji
            shortcode (str): Short code used to type the emoji
            image_url (str): URL of the image to use
            alt_text (str): Alt text (hover or screenreader) of the emoji
            keywords (List[str]): Keywords of the emoji.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Emoji created response
        """
        form={
            "category": category,
            "shortcode": shortcode,
            "image_url": image_url,
            "alt_text": alt_text,
            "keywords": keywords
            }
        res = self._req.lemmyRequest("createCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def edit(self, emoji_id:int, category:str=None, image_url:str=None, alt_text:str=None, keywords:List[str]=None, instance:str=None, auth_token:str=None):
        """
        Edit a custom emoji. Excluded optional arguments are not modified.
        
        Args:
            emoji_id (int): ID of the emoji
            category (str): Category of the emoji. Optional
            image_url (str): URL of the image to use. Optional
            alt_text (str): Alt text (hover or screenreader) of the emoji. Optional
            keywords (List[str]): Keywords of the emoji. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Emoji edited response
        """
        form={
            "id": emoji_id,
            "category": category,
            "image_url": image_url,
            "alt_text": alt_text,
            "keywords": keywords
            }
        res = self._req.lemmyRequest("editCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def delete(self, emoji_id:int, instance:str=None, auth_token:str=None):
        """
        Delete a custom emoji from the website
        
        Args:
            emoji_id (int): ID of emoji to delete
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Emoji deleted response
        """
        form={
            "id": emoji_id
            }
        res = self._req.lemmyRequest("deleteCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
