from .requestor import Requestor
from .api_paths import *
from jplaw.types import PostFeatureType

class Post():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def getPosts(self, community_id:int, sort:str=None, instance:str=None, auth:bool=True, auth_token:str=None):
        form = { "sort": sort or "New", "community_id": community_id }
        res = self._req.lemmyRequest("getPosts", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["posts"]
        
    def getPost(self, community_id, post_id, instance:str=None, auth=True, auth_token:str=None):
        form = {
            "id": post_id,
        }
        res = self._req.lemmyRequest("getPost", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["post_view"]
        
    def createPost(self, community_id:int, title:str=None, body:str=None, remote_url:str=None, nsfw=False, language_id=None, instance:str=None, auth_token:str=None):
        #there could be a bug here if instance != logged in instance when trying to create a post
        form = {
            "community_id": community_id,
            "name": title,
            "body": body,
            "language_id": language_id,
            "nsfw": nsfw
            }
        optional={
            "url": remote_url
        }
        res = self._req.lemmyRequest("createPost", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res["post_view"]
        
    def editPost(self, post_id:int, title:str=None, body:str=None, remote_url:str=None, nsfw:bool=None, language_id=None, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
        }
        optional={
            "url": remote_url,
            "nsfw": nsfw,
            "language_id": language_id,
            "name": name,
            "body": body
        }
        res = self._req.lemmyRequest("editPost", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res["post_view"]
        
    def likePost(self, post_id:int, score:int=1, language_id=None, instance:str=None, auth_token:str=None):
        if(score > 1):
            score = 1
        if(score < -1):
            score = -1
        form = {
            "post_id": post_id,
            "score": score
        }
        res = self._req.lemmyRequest("likePost", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def createPostReport(self, post_id:int, reason:str, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
            "reason": reason
            }
        res = self._req.lemmyRequest("createPostReport", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def deletePost(self, post_id:int, deleted:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
            "deleted": deleted
            }
        res = self._req.lemmyRequest("deletePost", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def featurePost(self, post_id:int, feature_type: PostFeatureType, featured:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
            "feature_type": feature_type.value,
            "featured": featured,
            }
        res = self._req.lemmyRequest("featurePost", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def listPostReports(self, page:int=None, limit:int=None, unresolved_only:bool=True, community_id:int=None, instance:str=None, auth_token:str=None):
        form = {}
        optional = {
            "page": page,
            "limit": limit,
            "unresolved_only": unresolved_only,
            "community_id": community_id,
            }
        res = self._req.lemmyRequest("listPostReports", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    
    def lockPost(self, post_id:int, locked:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
            "locked": locked,
        }
        res = self._req.lemmyRequest("lockPost", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def markPostAsRead(self, post_id:int, read:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
            "read": read,
        }
        res = self._req.lemmyRequest("markPostAsRead", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def resolvePostReport(self, report_id:int, resolved:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "report_id"  : report_id ,
            "resolved"   : resolved  ,
            }
        res = self._req.lemmyRequest("resolvePostReport", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return
        
    def savePost(self, post_id:int, save:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "post_id"  : post_id ,
            "save"   : save,
            }
        res = self._req.lemmyRequest("savePost", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return
        
    def getSiteMetadata(self, remote_url:str, instance:str=None, auth:bool=True, auth_token:str=None):
        form={
            "url": remote_url,
        }
        res = self._req.lemmyRequest("getSiteMetadata", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def removePost(self, post_id:int, mod_person_id:int, when_:str, removed:bool=True, reason:str=None, instance:str=None, auth_token:str=None):
        form = {
            "post_id": post_id,
            "mod_person_id": mod_person_id,
            "when_": when_,
            "removed": removed,
            }
        optional={
            "reason":reason,
            }
        res = self._req.lemmyRequest("removePost", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res["post_view"]