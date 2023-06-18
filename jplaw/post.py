from .requestor import Requestor, HttpType
from .api_paths import *

def listPosts(self, community_id, instance=None, sort=None, auth=True, auth_token=None):
    url = self.apiURL(self.instance, "listPosts")
    form = { "sort": sort or "New", "community_id": community_id }
    if(auth):
        form.auth = auth_token or self.auth_token
    res = self._req.request(
        HttpType.GET,
        url,
        form
    )
    
    return res["posts"]
def getPost(self, community_id, post_id, instance=None, auth=True, auth_token=None):
    url = self.apiURL(instance, "getPost")
    form = {
        "id": post_id,
    }
    if(auth):
        form["auth"] = auth_token or self.auth_token
    res = self._req.request(
        HttpType.GET,
        url,
        form,
    )
    return res["post_view"]

def submitPost(self, community_id, instance=None, title=None, body=None, remote_url=None, nsfw=False, language_id=None, auth_token=None):
    #there could be a bug here if instance != logged in instance when trying to create a post
    url = self.apiURL(instance, "submitPost")
    form = { 
        "auth": auth_token or self.auth_token, 
        "community_id": community_id,
        "name": title,
        "body": body,
        "language_id": language_id,
        "nsfw": nsfw
        }
    if(remote_url):
        form["url"] = remote_url
    res = self._req.request(
        HttpType.POST,
        url,
        form,
    )
    return res["post_view"]

def editPost(self, post_id, instance=None, title=None, body=None, remote_url=None, nsfw=None, language_id=None, auth_token=None):
    url = self.apiURL(instance, "editPost")
    form = {
        "auth": auth_token or self.auth_token,
        "post_id": post_id,
    }
    if(remote_url):
        form["url"] = remote_url
    if (not (nsfw is None)):
        form["nsfw"] = nsfw
    if (not (language_id is None)):
        form["language_id"] = language_id
    if title:
        form["name"] = title
    if body:
        form["body"] = body
    res = self._req.request(HttpType.PUT, url, form)
    return res["post_view"]

def likePost(self, post_id, score=1, instance=None, language_id=None, auth_token=None):
    url = self.apiURL(instance, "likePost")
    if(score > 1):
        score = 1
    if(score < -1):
        score = -1
    form = {
        "auth": auth_token or self.auth_token,
        "post_id": post_id,
        "score": score
    }
    res = self._req.request(HttpType.POST, url, form)
    return res