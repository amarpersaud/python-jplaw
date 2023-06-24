from .requestor import Requestor
from .api_paths import *


class Post():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def listPosts(self, community_id:int, sort:str=None, instance:str=None, auth:bool=True, auth_token:str=None):
        form = { "sort": sort or "New", "community_id": community_id }
        res = self._req.lemmyRequest("listPosts", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["posts"]
        
    def getPost(self, community_id, post_id, instance:str=None, auth=True, auth_token:str=None):
        form = {
            "id": post_id,
        }
        res = self._req.lemmyRequest("getPost", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res["post_view"]
        
    def submitPost(self, community_id:int, title=None, body=None, remote_url=None, nsfw=False, language_id=None, instance:str=None, auth_token:str=None):
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
        res = self._req.lemmyRequest("submitPost", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res["post_view"]
        
    def editPost(self, post_id:int, title=None, body=None, remote_url=None, nsfw=None, language_id=None, instance:str=None, auth_token:str=None):
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
