from .requestor import Requestor
from .comment import Comment
from .community import Community
from .post import Post
from .user import User
from .site import Site
from .private_message import PrivateMessage

class Lemmy:
    Post: Post
    """Post object. Allows Lemmy.Post functions"""
    Community: Community
    """Community object. Allows Lemmy.Community functions"""
    Comment: Comment
    """Comment object. Allows Lemmy.Comment functions"""
    User: User
    """User object. Allows Lemmy.User functions"""
    Site: Site
    """Site object. Allows Lemmy.Site functions"""
    PrivateMessage: PrivateMessage
    """PrivateMessage object. Allows Lemmy.PrivateMessage functions"""
    
    def __enter__(self):
        """Handle the context manager open."""
        return self
    
    def __exit__(self, *_args):
        """Handle the context manager close."""
    
    def __init__(self, instance:str, username:str = None, password:str = None):
        """
        Create a Lemmy object
        
        Args:
            instance (str): URL of instance to log in to or use
            username (str): username or email to log in with. Defaults to None (no authentication)
            password (str): password of user. Defaults to None (no authentication)
        Returns:
            Lemmy object
        """
        
        self.username = username
        
        # Login, get token, and set as header for future
        self._req = Requestor(instance=instance, username=username, password=password, headers={})
        
        self.Post = Post(self._req)
        self.Community = Community(self._req)
        self.Comment = Comment(self._req)
        self.User = User(self._req)
        self.Site = Site(self._req)
        self.PrivateMessage = PrivateMessage(self._req)
        # print(self._req.headers.get("Authorization"))
        
    def resolveObject(self, obj, instance:str=None, auth_token:str=None):
        """
        Resolves object from another instance
        
        Args:
            obj: Object to resolve from the remote instance
            instance (str): URL of local instance to request the object from
            auth_token (str): Authentication token for local instance
        Returns:
            Federated object
        """
        form={
            "q": obj
        }
        res = self._req.lemmyRequest("resolveObject", instance=instance, form=form, auth_token=auth_token)
        return res
        
    def search(self, term:str, instance:str=None, auth_token:str=None):
        """
        Search for term
        
        Args:
            term (str): Object to resolve from the remote instance
            instance (str): URL of local instance. Default None uses logged in instance
            auth_token (str): Authentication token for local instance
        Returns:
            Search results
        """
        form={
            "q": term
        }
        res = self._req.request("search", instance=instance, auth_token=auth_token, form=form)
        return res
