from .requestor import Requestor, HttpType
from .api_paths import *
from enum import *
from .comment import Comment
from .post import Post
from .user import User
from .site import Site

class Lemmy:
    Post: Post
    Community: Community
    Comment: Comment
    User: User
    Site: Site
    
    def __enter__(self):
        """Handle the context manager open."""
        return self
    
    def __exit__(self, *_args):
        """Handle the context manager close."""
    
    def __init__(self, instance, username:str = None, password:str = None):
        self.Post = Post()
        self.Community = Community()
        self.Comment = Comment()
        self.User = User()
        self.Site = Site()
        
        self.username = username
        
        # Login, get token, and set as header for future
        self._req = Requestor(instance=instance, username=username, password=password, headers={})
        
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
