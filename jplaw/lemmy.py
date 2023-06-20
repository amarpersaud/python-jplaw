from .requestor import Requestor, HttpType
from .api_paths import *

class Lemmy:    
    from .community import getCommunity, listCommunities, followCommunity
    from .post import listPosts, getPost, submitPost, editPost, likePost
    from .comment import submitComment, likeComment
    
    def __enter__(self):
        """Handle the context manager open."""
        return self
    
    def __exit__(self, *_args):
        """Handle the context manager close."""
    
    def __init__(self, instance, username, password):
        self.username = username
        
        # Login, get token, and set as header for future
        self._req = Requestor({})
        
        self.auth_token = self.login(username, password, instance)
        
        self._req.headers.update({"Authorization": "Bearer " + self.auth_token})
        # print(self._req.headers.get("Authorization"))
        
    def resolveObject(self, obj, instance=None, auth_token=None):
        form={
            "q": obj
        }
        res = self._req.lemmyRequest(HttpType.GET, "resolveObject", instance=instance, form=form, auth_token=auth_token)
        return res
        
    def search(self, term, instance=None, auth_token=None):
        form={
            "q": term
        }
        res = self._req.request(HttpType.GET, "search", instance=instance, auth_token=auth_token, form=form)
        return res
