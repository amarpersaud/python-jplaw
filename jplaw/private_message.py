from .requestor import Requestor
from .api_paths import *


class PrivateMessage():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def createPrivateMessage(self, content:str, recipient_id:int, instance:str=None, auth_token:str=None):
        form = {
            "content": content,
            "recipient_id": recipient_id,
            }
        res = self._req.lemmyRequest("createPrivateMessage", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def createPrivateMessageReport(self, private_message_id:int, reason:str, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            "reason": reason,
            }
        res = self._req.lemmyRequest("createPrivateMessageReport", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def editPrivateMessage(self, private_message_id:int, content:str, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            "content": content,
            }
        res = self._req.lemmyRequest("editPrivateMessage", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def deletePrivateMessage(self, private_message_id:int, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            }
        res = self._req.lemmyRequest("deletePrivateMessage", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def markPrivateMessageAsRead(self, private_message_id:int, read:bool=True, instance:str=None, auth_token:str=None):
        form = {
            "private_message_id": private_message_id,
            "read": read,
            }
        res = self._req.lemmyRequest("markPrivateMessageAsRead", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res