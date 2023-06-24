from .requestor import Requestor, HttpType
from .api_paths import *

class Community():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def getCommunity(self, name:str, instance:str=None, auth:bool=True, auth_token:str=None):
        form = {
            "name": name
        }
        res = self._req.lemmyRequest("getCommunity", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["community_view"]
        
    def listCommunities(self, instance:str=None, auth:bool=True, auth_token:str=None): 
        form={}
        res = self._req.lemmyRequest("listCommunities", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["communities"]
        
    def followCommunity(self, community_id:int, follow:bool=True, instance:str=None, auth_token:str=None):
        form={
            "community_id": community_id,
            "follow": follow
        }
        res = self._req.lemmyRequest("followCommunity", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["community_view"]
    def addModToCommunity(self, community_id:int, person_id:int, added:bool=True, instance:str=None, auth_token:str=None): 
        form={
            "community_id": community_id,
            "person_id": person_id,
            "added": added,
        }
        res = self._req.lemmyRequest("addModToCommunity", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    def addModToCommunity(self, community_id:int, person_id:int, added:bool=True, instance:str=None, auth_token:str=None):
        form={
            "community_id": community_id,
            "person_id": person_id,
            "added": added,
        }
        res = self._req.lemmyRequest("addModToCommunity", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def banFromCommunity(self, community_id:int, person_id:int, ban:bool, remove_data:bool=None, reason:str=None, expires:int=None, instance:str=None, auth_token:str=None):
        form={
            "community_id": community_id,
            "person_id": person_id,
            "ban": ban,
        }
        optional={
            "remove_data": remove_data,
            "reason": reason,
            "expires": expires,
        }
        res = self._req.lemmyRequest("addModToCommunity", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def blockCommunity(self, community_id:int, block:bool=True, instance:str=None, auth_token:str=None):
        form={
            "community_id": community_id,
            "block": block,
            }
        res = self._req.lemmyRequest("addModToCommunity", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def createCommunity(self, name:str, title:str, description:str=None, icon:str=None, banner:str=None, nsfw:bool=None, posting_restricted_to_mods:bool=None, discussion_languages:List[str]=None, instance:str=None, auth_token:str=None):
        form={
            "name": name,
            "title": title,
            }
        optional={
            "description": description,
            "icon": icon,
            "banner": banner,
            "nsfw": nsfw,
            "posting_restricted_to_mods": posting_restricted_to_mods,
            "discussion_languages": discussion_languages,
            }
        res = self._req.lemmyRequest("createCommunity", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    