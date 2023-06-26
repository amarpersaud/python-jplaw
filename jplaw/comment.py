from .requestor import Requestor
from .api_paths import *
from .types.listing_type import ListingType
from .types.comment_sort_type import CommentSortType

class Comment():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def create(self, post_id:int, content:str, parent_id:int=None, language_id:int=None, instance:str=None, auth_token:str=None):
        """
        Create a comment
        
        Args:
            post_id (int): ID of the post to create a comment on
            content (str): Contents of the comment
            parent_id (int): Parent comment ID. Optional. Default/If None, posts comment directly to post.
            language_id (int): Language ID
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        form = {
            "content": content,
            "post_id": post_id,
        }
        optional={
            "language_id": language_id,
            "parent_id": parent_id
        }
        res = self._req.lemmyRequest("createComment", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        
        return res["comment_view"]
        
    def like(self, comment_id:int, score:int=1, instance:str=None, auth_token:str=None):
        """
        Like a comment
        
        Args:
            comment_id (int): ID of the comment
            score (int): Score of the comment. -1/0/1 dislikes, removes like, and likes a comment.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        if(score > 1):
            score = 1
        if(score < -1):
            score = -1
        form = {
            "comment_id": comment_id,
            "score": score
        }
        res = self._req.lemmyRequest("likeComment", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def report(self, comment_id:int, reason:str, instance:str=None, auth_token:str=None):
        """
        Report a comment
        
        Args:
            comment_id (int): ID of the comment
            reason (str): Reason for reporting the comment
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment report response
        """
        form = {
            "comment_id": comment_id,
            "reason": reason
            }
        res = self._req.lemmyRequest("createCommentReport", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def delete(self, comment_id:int, deleted:bool=True, instance:str=None, auth_token:str=None):
        """
        Delete a comment
        
        Args:
            comment_id (int): ID of the comment
            deleted (bool): If comment is deleted. Optional. Defaults to true
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        form = {
            "comment_id": comment_id,
            "deleted": deleted
            }
        res = self._req.lemmyRequest("deleteComment", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def remove(self, comment_id:int, mod_person_id:int, when_:str, removed:bool=True, reason:str=None, instance:str=None, auth_token:str=None):
        """
        Moderator remove a comment
        
        Args:
            comment_id (int): ID of the comment
            mod_person_id (int): ID of the moderator removing the comment
            when_ (str): Timestamp for when the comment was removed
            removed (bool): If the comment is removed. Optional. Defaults to true.
            deleted (bool): If comment is deleted. Optional. Defaults to true
            reason (str): Reason for removing the comment. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        form = {
            "comment_id": comment_id,
            "mod_person_id": mod_person_id,
            "when_": when_,
            "removed": removed,
            }
        optional={
            "reason":reason,
            }
        res = self._req.lemmyRequest("removeComment", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def distinguish(self, comment_id:int, distinguished:bool=True, instance:str=None, auth_token:str=None):
        """
        Distinguish a comment
        
        Args:
            comment_id (int): ID of the comment
            distinguished (bool): If comment is distinguished. Optional. Defaults to true
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        form = {
            "comment_id": comment_id,
            "distinguished": distinguished,
            }
        res = self._req.lemmyRequest("distinguishComment", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def edit(self, comment_id:int, content:str=None, language_id:int=None, form_id:str=None, instance:str=None, auth_token:str=None):
        """
        Edit a comment
        
        Args:
            comment_id (int): ID of the comment
            content (str): content of the comment
            language_id (int): Language of the comment
            form_id (str): ???
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        form = {
            "comment_id": comment_id
            }
        optional={
            "content":content,
            "language_id":language_id,
            "form_id":form_id,
            }
        res = self._req.lemmyRequest("editComment", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def get(self, comment_id:int, instance:str=None, auth:bool=True, auth_token:str=None):    
        """
        Get a comment by id
        
        Args:
            comment_id (int): ID of the comment
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment response
        """
        form = {
            "comment_id": comment_id
            }
        res = self._req.lemmyRequest("getComment", instance=instance, form=form, optional=optional, auth=auth, auth_token=auth_token)
        return res["comment_view"]
        
    def list(self, 
        comment_type:ListingType=None, 
        sort:CommentSortType=None, 
        max_depth:int=None, 
        page:int=None, 
        limit:int=None, 
        community_id:int=None, 
        post_id:int=None, 
        community_name:str=None, 
        parent_id:int=None,
        saved_only:bool=None,
        instance:str=None, 
        auth:bool=True, 
        auth_token:str=None):
        """
        Get comments in a post
        
        Args:
            comment_id (int): ID of the comment
            comment_type (ListingType): Comment type. Optional.
            sort (CommentSortType): Sort type. Optional.
            max_depth (int): Max tree depth. Optional.
            page (int): Page number. Optional.
            limit (int): Comment count limit. Optional.
            community_id (int): ID of community to get comment from. Optional.
            post_id (int): ID of post to get comments from. Optional.
            community_name (str): Name of community to get comments from. Optional.
            parent_id (int): ID of parent comment to get replies to. Optional.
            saved_only (bool): Filter by only saved comments. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (bool): Whether or not to authenticate. Optional. True by default.
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment list
        """
        form = {
            "comment_id": comment_id
            }
        if(comment_type):
            form["type_"] = comment_type,
        if(sort):
            form["sort"] = sort

        optional={
            "max_depth"      : max_depth       ,
            "page"           : page            ,
            "limit"          : limit           ,
            "post_id"        : post_id         ,
            "community_id"   : community_id    ,
            "community_name" : community_name  ,
            "parent_id"      : parent_id       ,
            "saved_only"     : saved_only      ,
            }
       
        res = self._req.lemmyRequest("getComments", instance=instance, form=form, optional=optional, auth=auth, auth_token=auth_token)
        return res["comment_view"]
    
    def listReports(self, page:int=None, limit:int=None, unresolved_only:bool=None, community_id:int=None, instance:str=None, auth_token:str=None):
        """
        Get list of comment reports
        
        Args:
            page (int): Page number. Optional.
            limit (int): Comment count limit. Optional.
            unresolved_only (bool): If only unresolved reports should be listed. Optional.
            community_id (int): ID of community to get comment from. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment report list response
        """
        form = {}
        optional={
            "page"           : page            ,
            "limit"          : limit           ,
            "community_id"   : community_id    ,
            "unresolved_only": unresolved_only ,
            }
        res = self._req.lemmyRequest("listCommentReports", instance=instance, form=form, optional=optional, auth=auth, auth_token=auth_token)
        return
        
    def markReplyAsRead(self, comment_reply_id:int, read:bool=True, instance:str=None, auth_token:str=None):
        """
        Mark a reply as read
        
        Args:
            comment_reply_id (int): ID of comment reply.
            read (bool): If reply is marked as read. Optional. Defaults to True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Comment reply marked as read response
        """
        form = {
            "comment_reply_id"  : comment_reply_id  ,
            "read"              : read              ,
            }
        res = self._req.lemmyRequest("markCommentReplyAsRead", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return
    
    def resolveReport(self, report_id:int, resolved:bool=True, instance:str=None, auth_token:str=None):
        """
        Resolve a comment report
        
        Args:
            report_id (int): ID of report.
            resolved (bool): If reply is marked as read. Optional. Defaults to True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Report resolved response
        """
        form = {
            "report_id"  : report_id ,
            "resolved"   : resolved  ,
            }
        res = self._req.lemmyRequest("resolveCommentReport", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return
    
    def save(self, comment_id:int, save:bool=True, instance:str=None, auth_token:str=None):
        """
        Save a comment
        
        Args:
            comment_id (int): ID of comment.
            save (bool): If comment is saved or not. Optional. Defaults to True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Report resolved response
        """
        form = {
            "comment_id"  : comment_id ,
            "save"   : save,
            }
        res = self._req.lemmyRequest("saveComment", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return