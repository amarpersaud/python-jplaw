"""
Private message class. Used to access functions for sending, reading, and reporting private messages.
"""
from jplaw.requestor import Requestor
from jplaw.api_paths import *


class PrivateMessage():
    def __init__(self, _req: Requestor):
        self._req = _req
    
    def list(self, unread_only:bool=None, page:int=None, limit:int=None, instance:str=None):
        """
        Get list of private messages 
        
        Args:
            unread_only (bool): Filters private by unread. Optional.
            page (int): Page number of private messages. Optional.
            limit (int): Limit for number of private messages. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of private messages
        """
        form = {}
        optional={
            "unread_only": unread_only,
            "page": page,
            "limit": limit,
            }
        res = self._req.lemmyRequest("getPrivateMessages", instance=instance, form=form, optional=optional, auth=True)
        return res
    def create(self, content:str, recipient_id:int, instance:str=None):
        """
        Create and send a private message
        
        Args:
            content (str): Contents of private message
            recipient_id (int): User ID of recipient
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Sent private message response
        """
        form = {
            "content": content,
            "recipient_id": recipient_id,
            }
        res = self._req.lemmyRequest("createPrivateMessage", instance=instance, form=form, auth=True)
        return res
        
    def report(self, private_message_id:int, reason:str, instance:str=None):
        """
        Report a private message
        
        Args:
            private_message_id (int): ID of private message
            reason (str): Reason for reporting the private message
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Sent private message response
        """
        form = {
            "private_message_id": private_message_id,
            "reason": reason,
            }
        res = self._req.lemmyRequest("createPrivateMessageReport", instance=instance, form=form, auth=True)
        return res
        
    def edit(self, private_message_id:int, content:str, instance:str=None):
        """
        Edit a private message
        
        Args:
            private_message_id (int): ID of private message
            content (str): Contents of private message
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Private message response
        """
        form = {
            "private_message_id": private_message_id,
            "content": content,
            }
        res = self._req.lemmyRequest("editPrivateMessage", instance=instance, form=form, auth=True)
        return res
        
    def delete(self, private_message_id:int, instance:str=None):
        """
        Delete a private message
        
        Args:
            private_message_id (int): ID of private message
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Private message response
        """
        form = {
            "private_message_id": private_message_id,
            }
        res = self._req.lemmyRequest("deletePrivateMessage", instance=instance, form=form, auth=True)
        return res
        
    def markAsRead(self, private_message_id:int, instance:str=None):
        """
        Marks a private message as read
        
        Args:
            private_message_id (int): ID of private message
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Private message response
        """
        form={
            "private_message_id": private_message_id,
            }
        res = self._req.lemmyRequest("markPrivateMessageAsRead", instance=instance, form=form, auth=True)
        return res
        
    def listReports(self, page:int=None, limit:int=None, unresolved_only:bool=True, instance:str=None):
        """
        Gets list of private message reports
        
        Args:
            page (int): Page number
            limit (int): Limit for number of reports to get
            unresolved_only (bool): Get only unresolved posts. Default true gets only unresolved reports. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of private message reports
        """
        form = {}
        optional = {
            "page": page,
            "limit": limit,
            "unresolved_only": unresolved_only,
            }
        res = self._req.lemmyRequest("listPrivateMessageReports", instance=instance, form=form, optional=optional, auth=True)
        return res
    def resolveReport(self, report_id:int, resolved:bool=True, instance:str=None):
        """
        Resolve a private message report
        
        Args:
            report_id (int): Private message report ID
            resolved (bool): If private message report is reolved. Default true resolves report. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Private message report resolved response
        """
        form = {
            "report_id"  : report_id ,
            "resolved"   : resolved  ,
            }
        res = self._req.lemmyRequest("resolvePrivateMessageReport", instance=instance, form=form, auth=True)
        return res