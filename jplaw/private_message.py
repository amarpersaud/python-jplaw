from .requestor import Requestor
from .api_paths import *


class PrivateMessage():
    def __init__(self, _req: Requestor):
        self._req = _req
    
    def list(self, unread_only:bool=None, page:int=None, limit:int=None, instance:str=None, auth_token:str=None):
        form = {}
        optional={
            "unread_only": unread_only,
            "page": page,
            "limit": limit,
            }
        res = self._req.lemmyRequest("getPrivateMessages", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def create(self, content:str, recipient_id:int, instance:str=None, auth_token:str=None):
        form = {
            "content": content,
            "recipient_id": recipient_id,
            }
        res = self._req.lemmyRequest("createPrivateMessage", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def report(self, private_message_id:int, reason:str, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            "reason": reason,
            }
        res = self._req.lemmyRequest("createPrivateMessageReport", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def edit(self, private_message_id:int, content:str, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            "content": content,
            }
        res = self._req.lemmyRequest("editPrivateMessage", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def delete(self, private_message_id:int, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            }
        res = self._req.lemmyRequest("deletePrivateMessage", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def markAsRead(self, unread_only:bool=None, page:int=None, limit:int=None, instance:str=None, auth_token:str=None):
        form={}
        optional = {
            "unread_only": unread_only,
            "page": page,
            "limit": limit,
            }
        res = self._req.lemmyRequest("markPrivateMessageAsRead", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def listReports(self, page:int=None, limit:int=None, unresolved_only:bool=True, instance:str=None, auth_token:str=None):
        form = {}
        optional = {
            "page": page,
            "limit": limit,
            "unresolved_only": unresolved_only,
            }
        res = self._req.lemmyRequest("listPrivateMessageReports", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def resolveReport(self, report_id:int, resolved:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "report_id"  : report_id ,
            "resolved"   : resolved  ,
            }
        res = self._req.lemmyRequest("resolvePrivateMessageReport", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return