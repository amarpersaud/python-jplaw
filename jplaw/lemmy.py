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
    
    def apiURL(self, instance, path):
        url = instance or self.instance
        return url.rstrip("/") + API_VERSION.rstrip("/") + API_PATH[path]
    
    def login(self, username, password, instance=None):
        self.instance = instance or self.instance 
        url = self.apiURL(self.instance, "login")
        form = {"username_or_email": username, "password": password}
        res_data = self._req.request(HttpType.POST, url, form)
        return res_data["jwt"]
        
    def resolveObject(self, obj, instance=None, auth_token=None):
        url = self.apiURL(instance, "resolveObject")
        form={
            "q": obj,
            "auth": auth_token or self.auth_token
        }
        res = self._req.request(HttpType.GET, url, form)
        return res
        
    def search(self, term, instance=None, auth_token=None):
        url = self.apiURL(instance, "search")
        form={
            "q": term,
            "auth": auth_token or self.auth_token
        }
        res = self._req.request(HttpType.GET, url, form)
        return res