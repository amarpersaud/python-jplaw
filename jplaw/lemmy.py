"""
The Lemmy object is used to interract with a Lemmy instance.

Creation can be done 

```python
import jplaw

my_instance = "..."
my_username = "..."
my_password = "..."

lem = jplaw.Lemmy(
    instance=my_instance, 
    username=my_username, 
    password=my_password
    )
```

Functions of subtypes can be done like so:

```python
print(lem.Community.list())

print(lem.Post.create(community_id=..., title="Test", body="test"))
```

"""

from jplaw.requestor import Requestor
from jplaw.comment import Comment
from jplaw.community import Community
from jplaw.post import Post
from jplaw.user import User
from jplaw.site import Site
from jplaw.emoji import Emoji
from jplaw.private_message import PrivateMessage

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
        self.Emoji = Emoji(self._req)
        self.PrivateMessage = PrivateMessage(self._req)
        # print(self._req.headers.get("Authorization"))
        
    def federateCommunity(self, name:str, auth:bool=True, instance:str=None):
        """
        Get comunity from another instance which may not have been federated.
        
        Args:
            name (str): Name of the community. Include @[instance] for a community at 
            auth (bool): Whether or not to use authentication. True by default.
            instance (str): Remote instance to send federation command to / get federated community through. Federating "[community]@[instance A]" with instance="[instance B]" sends the federation command to instance B, which then looks for the community at instance A. Default None uses instane = logged in instance.
        
        Returns:
            Community 
        """
        data = self.Site.resolveObject("!" + name);
        return self.Community.get(name, instance=instance, auth=auth)["community_view"];
