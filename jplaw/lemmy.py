from .requestor import Requestor, HttpType

class Lemmy:
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
        if(instance):
            self.instance = instance 
        url = apiURL(self.instance, "login")
        res_data = self._req.request(HttpType.POST, url, {"username_or_email": username, "password": password})
        return res_data["jwt"]
    
    def getCommunity(self, name, instance=None, auth=False, auth_token=None):
        url = apiURL(instance, "getCommunity")
        form = {"name": name}
        if(auth):
            form.data = auth_token or self.auth_token
        res = self._req.request(HttpType.GET, url, form)
        return self.community

    def listCommunities(self, instance=None, auth=False, auth_token=None): 
        url = apiURL(self.instance, "listCommunities")
        form={}
        if(auth):
            form.data = auth_token or self.auth_token
        res = self._req.request(HttpType.GET, url, form)
        return res

    def listPosts(self, community_id, instance=None, sort=None, auth=False, auth_token=None):
        url = apiURL(self.instance, "listPosts")
        form = { "sort": sort or "New", "community_id": community_id }
        if(auth):
            form.data = auth_token or self.auth_token
        res = self._req.request(
            HttpType.GET,
            url,
            form
        )
        
        return res["posts"]

    def getPost(self, community_id, post_id, instance=None, auth=False, auth_token=None):
        url = apiURL(instance, "getPost")
        form = {"id": post_id}
        if(auth):
            form.data = auth_token or self.auth_token
        res = self._req.request(
            HttpType.GET,
            url,
            form,
        )
        
        return res["post_view"]

    def submitPost(self, title=None, body=None, url=None):
        api_url = self.instance + "/api/v3/post"
        res = self._req.request(
            HttpType.POST,
            api_url,
            {
                "auth": self.auth_token,
                "community_id": self.community["id"],
                "name": title,
                "body": body,
                "url": url,
            },
        )
        
        return res["post_view"]

    def editPost(self, post_id, title=None, body=None, url=None):
        api_url = self.instance + "/api/v3/post"
        data = {
            "auth": self.auth_token,
            "post_id": post_id,
        }
        if title:
            data["name"] = title
        if body:
            data["body"] = body
        if url:
            data["url"] = url
        
        res = self._req.request(HttpType.PUT, api_url, data)
        
        return res["post_view"]

    def submitComment(self, post_id, content, language_id=None, parent_id=None):
        api_url = self.instance + "/api/v3/comment"

        data = {
            "auth": self.auth_token,
            "content": content,
            "post_id": post_id,
        }
        
        if language_id:
            data["language_id"] = language_id
        if parent_id:
            data["parent_id"] = parent_id
        
        res = self._req.request(
            HttpType.POST,
            api_url,
            data,
        )
        
        return res
