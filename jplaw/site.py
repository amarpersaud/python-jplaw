from .requestor import Requestor, HttpType
from .api_paths import *

class Site():
    def __init__(self, _req: Requestor):
        self._req = _req
    
    def getSite(self, instance=None, auth=True, auth_token=None):
        form = {}
        res = self._req.lemmyRequest(HttpType.GET, "getSite", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
    
    def createSite(self, instance=None, auth=True, auth_token=None, form={}):
        res = self._req.lemmyRequest(HttpType.POST, "createSite", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
    
    def editSiteself, instance=None, auth=True, auth_token=None, form={}):
        res = self._req.lemmyRequest(HttpType.PUT, "editSite", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
