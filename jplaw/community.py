from .requestor import Requestor, HttpType
from .api_paths import *

class Community():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def getCommunity(self, name, instance:str=None, auth=True, auth_token:str=None):
        form = {
            "name": name
        }
        res = self._req.lemmyRequest("getCommunity", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["community_view"]
        
    def listCommunities(self, instance:str=None, auth=True, auth_token:str=None): 
        form={}
        res = self._req.lemmyRequest("listCommunities", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["communities"]
        
    def followCommunity(self, community_id, follow=True, instance:str=None, auth_token:str=None):
        form={
            "community_id": community_id,
            "follow": follow
        }
        res = self._req.lemmyRequest("followCommunity", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["community_view"]
