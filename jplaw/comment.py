from .requestor import Requestor
from .api_paths import *

class Comment():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def submitComment(self, post_id, content, parent_id=None, instance=None, language_id=None, auth_token=None):
        url = self.apiURL("submitComment")
        
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
        
    def likeComment(self, comment_id, score=1, instance=None, auth_token=None):
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
