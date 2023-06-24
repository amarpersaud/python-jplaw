from .requestor import Requestor
from .api_paths import *
from typing import List

class Site():
    def __init__(self, _req: Requestor):
        self._req = _req
    
    def getSite(self, instance:str=None, auth:bool=True, auth_token:str=None):
        form = {}
        res = self._req.lemmyRequest("getSite", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
    
    def createSite(self, instance:str=None, auth_token:str=None, form={}):
        res = self._req.lemmyRequest("createSite", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def editSite(self, instance:str=None, auth_token:str=None, form={}):
        res = self._req.lemmyRequest("editSite", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def getFederatedInstances(self, instance:str=None, auth:bool=True, auth_token:str=None):
        res = self._req.lemmyRequest("federated_instances", instance=instance, auth=auth, auth_token=auth_token)
        return res
        
    def createCustomEmoji(self, category:str, shortcode:str, image_url:str, alt_text:str, keywords:List[str], instance:str=None, auth_token:str=None):
        form={
            "category": category,
            "shortcode": shortcode,
            "image_url": image_url,
            "alt_text": alt_text,
            "keywords": keywords
            }
        res = self._req.lemmyRequest("createCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def editCustomEmoji(self, emoji_id:int, category:str=None, image_url:str=None, alt_text:str=None, keywords:List[str]=None, instance:str=None, auth_token:str=None):
        form={
            "id": emoji_id,
            "category": category,
            "image_url": image_url,
            "alt_text": alt_text,
            "keywords": keywords
            }
        res = self._req.lemmyRequest("editCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def deleteCustomEmoji(self, emoji_id:int, instance:str=None, auth_token:str=None):
        form={
            "id": emoji_id
            }
        res = self._req.lemmyRequest("deleteCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res

    def addAdmin(self, person_id:int, added:bool, instance:str=None, auth_token:str=None):
        form={
            "person_id": person_id,
            "added": added
            }
        res = self._req.lemmyRequest("addAdmin", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def getUnreadRegistrationApplicationCount(self, instance:str=None, auth_token=None):
        form={}
        res = self._req.lemmyRequest("getUnreadRegistrationApplicationCount", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def listRegistrationApplications(self, unread_only:bool=None, page:int=None, limit:str=None, instance:str=None, auth_token=None):
        form={}
        optional={
            "page": page,
            "limit": limit,
            "unread_only": unread_only
            }
        res = self._req.lemmyRequest("listRegistrationApplications", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res