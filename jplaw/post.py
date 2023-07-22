"""
Post class. Designed to allow Lemmy.Post functions.
"""
from jplaw.requestor import Requestor
from jplaw.api_paths import *
from jplaw.types.post_feature_type import PostFeatureType
from jplaw.types.listing_type import ListingType
from jplaw.types.sort_type import SortType

class Post():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def list(
        self, 
        type:ListingType=None, 
        sort:SortType=None, 
        page:int=None, 
        limit:int=None, 
        community_id:int=None, 
        community_name:str=None, 
        saved_only:bool=None, 
        moderator_view: bool=None,
        instance:str=None, 
        auth:bool=True):
        """
        Get a list of posts in a community
        
        Args:
            type (ListingType): Type of post. Optional
            sort (SortType): Sorting Mode. Optional
            page (int): Page number. Optional
            limit (int): Limit for number of posts. Optional
            community_id (int): ID of the community the post is in. Optional
            community_name (str): Name of the community the post is in. Optional
            saved_only (bool): Find posts only from saved posts. Optional
            moderator_view (bool): Moderator view. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (str): If true, authenticates using internal token from login. Optional. Default True
        Returns:
            List of posts
        """
        form = {}
        optional = {
            "sort": sort,
            "type": type,
            "community_id": community_id,
            "page": page,
            "limit": limit,
            "community_name": community_name,
            "saved_only": saved_only,
            "moderator_view": moderator_view,
            }
        res = self._req.lemmyRequest("getPosts", instance=instance, form=form, optional=optional, auth=auth)
        return res["posts"]
        
    def get(self, post_id:int=None, comment_id:int=None, instance:str=None, auth:bool=True):
        """
        Get a post by ID
        
        Args:
            post_id (int): ID of the post. Optional
            comment_id (int): Comment ID for comment view. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (str): If true, authenticates using internal token from login. Optional. Default True
        Returns:
            Post response
        """
        form = {}
        optional = {
            "id": post_id,
            "comment_id": comment_id,
            }
        res = self._req.lemmyRequest("getPost", instance=instance, form=form, optional=optional, auth=auth)
        
        return res["post_view"]
        
    def create(self, community_id:int, title:str=None, body:str=None, remote_url:str=None, honeypot:str=None, nsfw:bool=False, language_id:int=None, instance:str=None):
        """
        Create a post
        
        Args:
            community_id (int): ID of the community the post is in. Optional
            title (str): Title of the post. Optional.
            body (str): Text contents of the post. Optional
            remote_url (str): URL if link post. Optional.
            nsfw (bool): NSFW post. Optional. Defaults to false.
            language_id (int): Language ID
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Created post response
        """
        form = {}
        optional={
            "url": remote_url,
            "community_id": community_id,
            "name": title,
            "body": body,
            "language_id": language_id,
            "nsfw": nsfw,
            "honeypot": honeypot
            }
        res = self._req.lemmyRequest("createPost", instance=instance, form=form, optional=optional, auth=True)
        return res["post_view"]
        
    def edit(self, post_id:int, title:str=None, body:str=None, remote_url:str=None, nsfw:bool=None, language_id:int=None, instance:str=None):
        """
        Edit a post
        
        Args:
            post_id (int): ID of the post to edit
            title (str): Title of the post. Optional.
            body (str): Text contents of the post. Optional
            remote_url (str): URL if link post. Optional.
            nsfw (bool): NSFW post. Optional. Defaults to None.
            language_id (int): Language ID
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Edited post response
        """
        form = {
            "post_id": post_id,
        }
        optional={
            "url": remote_url,
            "nsfw": nsfw,
            "language_id": language_id,
            "name": title,
            "body": body
        }
        res = self._req.lemmyRequest("editPost", instance=instance, form=form, optional=optional, auth=True)
        return res["post_view"]
        
    def like(self, post_id:int, score:int=1, instance:str=None):
        """
        Like a post
        
        Args:
            post_id (int): ID of the post
            score (int)::1 for like, -1 for dislike, 0 to remove like. Clamped to 1/0/-1.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Liked post response
        """
        if(score > 1):
            score = 1
        if(score < -1):
            score = -1
        form = {
            "post_id": post_id,
            "score": score
            }
        res = self._req.lemmyRequest("likePost", instance=instance, form=form, auth=True)
        return res
    
    def report(self, post_id:int, reason:str, instance:str=None):
        """
        Report a post
        
        Args:
            post_id (int): ID of the post
            reason (str): Reason for reporting the post
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Reported post response
        """
        form = {
            "post_id": post_id,
            "reason": reason
            }
        res = self._req.lemmyRequest("createPostReport", instance=instance, form=form, auth=True)
        return res
        
    def delete(self, post_id:int, deleted:bool=True, instance:str=None):
        """
        Delete a post
        
        Args:
            post_id (int): ID of the post
            deleted (bool): If post is deleted. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Deleted post response
        """
        form = {
            "post_id": post_id,
            "deleted": deleted
            }
        res = self._req.lemmyRequest("deletePost", instance=instance, form=form, auth=True)
        return res
        
    def feature(self, post_id:int, feature_type: PostFeatureType, featured:bool=True, instance:str=None):
        """
        Feature a post
        
        Args:
            post_id (int): ID of the post
            feature_type (PostFeatureType): Type of featured post. Currently Community and Local.
            featured (bool): If post is featured or not. Optional. Defaults to True.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Featured post response
        """
        form = {
            "post_id": post_id,
            "featured": featured,
            }
        if(feature_type):
            form["feature_type"] = feature_type.value
        res = self._req.lemmyRequest("featurePost", instance=instance, form=form, auth=True)
        return res
        
    def listReports(self, page:int=None, limit:int=None, unresolved_only:bool=True, community_id:int=None, instance:str=None):
        """
        Get list of post reports
        
        Args:
            page (int): Page number. Optional
            limit (int): Limit for number of posts. Optional
            unresolved_only (bool): If only unresolved posts should be shown. Optional
            community_id (int): ID of the community to filter reports from. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of reported posts
        """
        form = {}
        optional = {
            "page": page,
            "limit": limit,
            "unresolved_only": unresolved_only,
            "community_id": community_id,
            }
        res = self._req.lemmyRequest("listPostReports", instance=instance, form=form, optional=optional, auth=True)
        return res
    
    def lock(self, post_id:int, locked:bool=True, instance:str=None):
        """
        Lock a post
        
        Args:
            post_id (int): ID of the post
            locked (bool): If post is locked. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Locked post response
        """
        form = {
            "post_id": post_id,
            "locked": locked,
        }
        res = self._req.lemmyRequest("lockPost", instance=instance, form=form, auth=True)
        return res
        
    def markAsRead(self, post_id:int, read:bool=True, instance:str=None):
        """
        Mark a post as read
        
        Args:
            post_id (int): ID of the post
            read (bool): If post is read. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Read post response
        """
        form = {
            "post_id": post_id,
            "read": read,
        }
        res = self._req.lemmyRequest("markPostAsRead", instance=instance, form=form, auth=True)
        return res
    
    def resolveReport(self, report_id:int, resolved:bool=True, instance:str=None):
        """
        Resolve a post report
        
        Args:
            report_id (int): ID of the post report
            resolved (bool): If post report is resolved. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Post report resolved response
        """
        form = {
            "report_id"  : report_id ,
            "resolved"   : resolved  ,
            }
        res = self._req.lemmyRequest("resolvePostReport", instance=instance, form=form, auth=auth)
        return
        
    def save(self, post_id:int, save:bool=True, instance:str=None):
        """
        Save a post
        
        Args:
            post_id (int): ID of the post
            save (bool): If post is saved. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Post report resolved response
        """
        form = {
            "post_id"  : post_id ,
            "save"   : save,
            }
        res = self._req.lemmyRequest("savePost", instance=instance, form=form, auth=auth)
        return
        
    def getSiteMetadata(self, remote_url:str, instance:str=None, auth:bool=True):
        """
        Gets metadata for a site when linked by a post
        
        Args:
            remote_url (str): URL of the site to get the metadata for
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Post report resolved response
        """
        form={
            "url": remote_url,
        }
        res = self._req.lemmyRequest("getSiteMetadata", instance=instance, form=form, auth=auth)
        return res
        
    def remove(self, post_id:int, mod_person_id:int, when_:str, removed:bool=True, reason:str=None, instance:str=None):
        """
        Remove a post as a moderator
        
        Args:
            post_id (int): ID of the post to remove
            mod_person_id (int): ID of the moderator removing the post
            when_ (str): Timestamp of when post was removed
            removed (bool): If post is removed. Optional. Defaults to True.
            reason (str): Reason for post removal. Optional. 
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Post report resolved response
        """
        form = {
            "post_id": post_id,
            "mod_person_id": mod_person_id,
            "when_": when_,
            "removed": removed,
            }
        optional={
            "reason":reason,
            }
        res = self._req.lemmyRequest("removePost", instance=instance, form=form, optional=optional, auth=True)
        return res["post_view"]
