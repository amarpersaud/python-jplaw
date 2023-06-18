from .requestor import Requestor, HttpType
from .api_paths import *

def getCommunity(self, name, instance=None, auth=True, auth_token=None):
    url = self.apiURL(instance, "getCommunity")
    form = {"name": name}
    if(auth):
        form["auth"] = auth_token or self.auth_token
    res = self._req.request(HttpType.GET, url, form)
    return res["community_view"]

def listCommunities(self, instance=None, auth=True, auth_token=None): 
    url = self.apiURL(instance, "listCommunities")
    form={}
    if(auth):
        form["auth"] = auth_token or self.auth_token
    res = self._req.request(HttpType.GET, url, form)
    return res["communities"]

def followCommunity(self, community_id, follow=True, instance=None, auth_token=None):
    url = self.apiURL(instance, "followCommunity")
    form={
        "community_id": community_id,
        "follow": follow,
        "auth": auth_token or self.auth_token
    }
    res = self._req.request(HttpType.POST, url, form)
    return res["community_view"]