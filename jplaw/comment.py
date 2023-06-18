from .requestor import Requestor, HttpType
from .api_paths import *

def submitComment(self, post_id, content, parent_id=None, instance=None, title=None, body=None, remoteinstance=None, nsfw=None, language_id=None, auth_token=None):
    url = self.apiURL(instance, "submitComment")
    
    data = {
        "auth": self.auth_token,
        "content": content,
        "post_id": post_id,
        "url": remoteinstance or url
    }
    
    if language_id:
        data["language_id"] = language_id
    if parent_id:
        data["parent_id"] = parent_id
    
    res = self._req.request(
        HttpType.POST,
        url,
        data,
    )
    
    return res