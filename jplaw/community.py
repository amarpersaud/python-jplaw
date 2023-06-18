from .requestor import Requestor, HttpType
from .api_paths import *

def getCommunity(self, name, instance=None, auth=False, auth_token=None):
    url = self.apiURL(instance, "getCommunity")
    form = {"name": name}
    if(auth):
        form.auth = auth_token or self.auth_token
    res = self._req.request(HttpType.GET, url, form)
    return res["community_view"]["community"]

def listCommunities(self, instance=None, auth=False, auth_token=None): 
    url = self.apiURL(self.instance, "listCommunities")
    form={}
    if(auth):
        form.auth = auth_token or self.auth_token
    res = self._req.request(HttpType.GET, url, form)
    return res["communities"]