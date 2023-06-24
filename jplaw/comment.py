from .requestor import Requestor
from .api_paths import *

class Comment():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def createComment(self, post_id:int, content:str, parent_id:int=None, language_id:str=None, instance:str=None, auth_token:str=None):
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
        
    def likeComment(self, comment_id:int, score:int=1, instance:str=None, auth_token:str=None):
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
        
    def createCommentReport(self, comment_id:int, reason:str, instance:str=None, auth_token:str=None):
        form = {
            "comment_id": comment_id,
            "reason": reason
            }
        res = self._req.lemmyRequest("createCommentReport", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def deleteComment(self, comment_id:int, deleted:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "comment_id": comment_id,
            "deleted": deleted
            }
        res = self._req.lemmyRequest("deleteComment", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def removeComment(self, comment_id:int, mod_person_id:int, when_:str, removed:bool=True, reason:str=None, instance:str=None, auth_token:str=None):
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
        
    def distinguishComment(self, comment_id:int, distinguished:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "comment_id": comment_id,
            "distinguished": distinguished,
            }
        res = self._req.lemmyRequest("distinguishComment", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res["comment_view"]
        
    def editComment(self, comment_id:int, content:str=None, language_id:str=None, form_id:str=None, instance:str=None, auth_token:str=None):
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
    
    def getComment(self, comment_id:int, instance:str=None, auth:bool=True, auth_token:str=None):
        form = {
            "comment_id": comment_id
            }
        res = self._req.lemmyRequest("getComment", instance=instance, form=form, optional=optional, auth=auth, auth_token=auth_token)
        return res["comment_view"]
    def getComments(self, 
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
        form = {
            "comment_id": comment_id
            }
        optional={
            "comment_type"   : comment_type    ,
            "sort"           : sort            ,
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
    
    def listCommentReports(self, page:int=None, limit:int=None, unresolved_only:bool=None, community_id:int=None, instance:str=None, auth_token:str=None):
        form = {}
        optional={
            "page"           : page            ,
            "limit"          : limit           ,
            "community_id"   : community_id    ,
            "unresolved_only": unresolved_only ,
            }
        res = self._req.lemmyRequest("listCommentReports", instance=instance, form=form, optional=optional, auth=auth, auth_token=auth_token)
        return
        
    def markCommentReplyAsRead(self, comment_reply_id:int, read:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "comment_reply_id"  : comment_reply_id  ,
            "read"              : read              ,
            }
        res = self._req.lemmyRequest("markCommentReplyAsRead", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return
    
    def resolveCommentReport(self, report_id:int, resolved:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "report_id"  : report_id ,
            "resolved"   : resolved  ,
            }
        res = self._req.lemmyRequest("resolveCommentReport", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return
    
    def saveComment(self, comment_id:int, save:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "comment_id"  : comment_id ,
            "save"   : save,
            }
        res = self._req.lemmyRequest("saveComment", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return