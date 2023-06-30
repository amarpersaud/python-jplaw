from .requestor import Requestor
from .comment import Comment
from .community import Community
from .post import Post
from .user import User
from .site import Site
from .emoji import Emoji
from .private_message import PrivateMessage

class Lemmy:
    """
    Lemmy object. Used to interract with a lemmy site
    """
    
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
    Emoji: Emoji
    """Emoji object. Allows Lemmy.Emoji functions"""
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
        
        # Create objects for function access
        self.Post = Post(self._req)
        self.Community = Community(self._req)
        self.Comment = Comment(self._req)
        self.User = User(self._req)
        self.Site = Site(self._req)
        this.Emoji = Emoji(self._req)
        self.PrivateMessage = PrivateMessage(self._req)
        # print(self._req.headers.get("Authorization"))
