from .requestor import Requestor, HttpType
from .api_paths import *

def getCommunity(self, name, instance=None, auth=True, auth_token=None):
    form = {"name": name}
    res = self._req.lemmyRequest(HttpType.GET, "getCommunity", instance=instance, form=form, auth=auth, auth_token=auth_token)
    return res["community_view"]

def listCommunities(self, instance=None, auth=True, auth_token=None): 
    form={}
    res = self._req.lemmyRequest(HttpType.GET, "listCommunities", instance=instance, form=form, auth=auth, auth_token=auth_token)
    return res["communities"]

def followCommunity(self, community_id, follow=True, instance=None, auth_token=None):
    form={
        "community_id": community_id,
        "follow": follow
    }
    res = self._req.lemmyRequest(HttpType.POST, "followCommunity", instance=instance, form=form, auth=True, auth_token=auth_token)
    return res["community_view"]
