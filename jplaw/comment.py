from .requestor import Requestor
from .api_paths import *

class Comment():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def submitComment(self, post_id:int, content:str, parent_id:int=None, language_id:str=None, instance:str=None, auth_token:str=None):
        form = {
            "content": content,
            "post_id": post_id,
        }
        optional={
            "language_id": language_id,
            "parent_id": parent_id
        }
        res = self._req.lemmyRequest("submitComment", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        
        return res["comment_view"]
        
    def likeComment(self, comment_id:int, score=1, instance:str=None, auth_token:str=None):
        if(score > 1):
            score = 1
        if(score < -1):
            score = -1
        form = {
            "comment_id": comment_id,
            "score": score
        }
        res = self._req.lemmyRequest("likeComment", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["comment_view"]
