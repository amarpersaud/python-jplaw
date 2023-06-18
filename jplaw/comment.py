from .requestor import Requestor, HttpType
from .api_paths import *

def submitComment(self, post_id, content, parent_id=None, instance=None, language_id=None, auth_token=None):
    url = self.apiURL(instance, "submitComment")
    
    form = {
        "auth": auth_token or self.auth_token,
        "content": content,
        "post_id": post_id,
    }
    
    if language_id:
        form["language_id"] = language_id
    if parent_id:
        form["parent_id"] = parent_id
    
    res = self._req.request(
        HttpType.POST,
        url,
        form,
    )
    
    return res