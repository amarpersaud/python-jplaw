from .requestor import Requestor
from .api_paths import *
from typing import List

class User():
    def __init__(self, _req: Requestor):
        self._req = _req
    def leaveAdmin(self, instance:str=None, auth_token:str=None):
        form = {}
        res = self._req.lemmyRequest("leaveAdmin", instance=instance, form=form, auth=True, auth_token=auth_token)
    def register(self, username:str, password:str, password_verify:str, show_nsfw:bool, email:str=None, captcha_uuid:str=None, captcha_answer:str=None, honeypot:str=None, answer:str=None, instance:str=None):
        form={
            "username": username,
            "password": password,
            "password_verify": password_verify,
            "show_nsfw": show_nsfw
            }
        optional = {       
            "email"          :email          ,
            "captcha_uuid"   :captcha_uuid   ,
            "captcha_uuid"   :captcha_uuid   ,
            "limit"          :limit          ,
            "honeypot"       :honeypot       ,
            "answer"         :answer         ,
            }
        res = self._req.lemmyRequest("register", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def getPersonDetails(self, person_id:str=None, username:str=None, sort:str=None, page:int=0, limit:int=10, community_id:int=None, saved_only:bool=None, instance:str=None, auth:bool=True, auth_token:str=None):
        form={}
        optional={
            "person_id"      :person_id      ,
            "username"       :username       ,
            "sort"           :sort           ,
            "page"           :page           ,
            "limit"          :limit          ,
            "community_id"   :community_id   ,
            "saved_only"     :saved_only     ,
            }
        res = self._req.lemmyRequest("getPersonDetails", instance=instance, form=form, optional=optional, auth=auth, auth_token=auth_token)
        return res
    
    def markPersonMentionAsRead(self, person_mention_id:int, read:bool=True, instance:str=None, auth_token:str=None):
        form={
            "person_mention_id": person_mention_id,
            "read": read
            }
        res = self._req.lemmyRequest("markPersonMentionAsRead", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def getPersonMentions(self, sort:str=None, page:int=0, limit:int=10, unread_only:bool=True, instance:str=None, auth_token:str=None):
        form={}
        optional = {
            "sort"           :sort           ,
            "page"           :page           ,
            "limit"          :limit          ,
            "unread_only"    :unread_only    ,
            }
        res = self._req.lemmyRequest("getPersonMentions", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    
    def getReplies(self, sort:str=None, page:int=0, limit:int=10, unread_only:bool=True, auth_token:str=None):
        form={}
        optional = {
            "sort"           :sort           ,
            "page"           :page           ,
            "limit"          :limit          ,
            "unread_only"    :unread_only    ,
            }
        res = self._req.lemmyRequest("getReplies", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    
    def banPerson(self, person_id:int, ban:bool, remove_data:bool=None, reason:str=None, expires:int=None, instance:str=None, auth_token:str=None):
        form={
            "person_id"     :person_id,
            "ban"           :ban
            }
        optional = {
            "remove_data"    :remove_data   ,
            "reason"         :reason        ,
            "expires"        :expires
            }
        res = self._req.lemmyRequest("banPerson", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    
    def getBannedPersons(self, instance:str=None, auth_token:str=None):
        form={}
        res = self._req.lemmyRequest(HttpType.GET, "getBannedPersons", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
     
    def blockPerson(self, person_id:int, block:bool, instance:str=None, auth_token:str=None):
        form={
            "person_id": person_id,
            "block": block
            }
        res = self._req.lemmyRequest("blockPerson", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def getCaptcha(self, instance:str=None, auth_token:str=None):
        form={}
        res = self._req.lemmyRequest("getCaptcha", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def deleteAccount(self, password, instance:str=None, auth_token:str=None):
        form={
            "password": password
            }
        res = self._req.lemmyRequest("deleteAccount", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
    
    def passwordReset(self, email, instance:str=None, auth_token:str=None):
        form={
            "email": email
            }
        res = self._req.lemmyRequest("passwordReset", instance=instance, form=form, auth=False, auth_token=auth_token)
        return res
        
    def passwordChangeAfterReset(self, token:str, password:str, password_verify:str, instance:str=None, auth_token:str=None):
        form={
            "token": token,
            "password": password,
            "password_verify": password_verify
            }
        res = self._req.lemmyRequest("passwordChangeAfterReset", instance=instance, form=form, auth=False, auth_token=auth_token)
        return res
        
    def markAllAsRead(self, community_view:str=None, site:str=None, moderators:List[str]=None, discussion_languages:List[str]=None, instance:str=None, auth_token:str=None):
        form={}
        optional={
            "community_view": community_view,
            "site": site,
            "moderators": moderators,
            "discussion_languages": discussion_languages,
            }
        res = self._req.lemmyRequest("markAllAsRead", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def saveUserSettings(self,
        show_nsfw: bool=None,
        show_scores: bool=None,
        theme: str=None,
        default_sort_type: str=None,
        default_listing_type: str=None,
        interface_language: str=None,
        avatar: str=None,
        banner: str=None,
        display_name: str=None,
        email: str=None,
        bio: str=None,
        matrix_user_id: str=None,
        show_avatars: bool=None,
        send_notifications_to_email: bool=None,
        bot_account: bool=None,
        show_bot_accounts: bool=None,
        show_read_posts: bool=None, 
        show_new_post_notifs: bool=None, 
        discussion_languages: List[str]=None, 
        generate_totp_2fa: bool=None, 
        instance:str=None,
        auth_token:str=None):
        form = {}
        optional = {
            "show_nsfw"                     : show_nsfw                  ,
            "show_scores"                   : show_scores                ,
            "theme"                         : theme                      ,
            "default_sort_type"             : default_sort_type          ,
            "default_listing_type"          : default_listing_type       ,
            "interface_language"            : interface_language         ,
            "avatar"                        : avatar                     ,
            "banner"                        : banner                     ,
            "display_name"                  : display_name               ,
            "email"                         : email                      ,
            "bio"                           : bio                        ,
            "matrix_user_id"                : matrix_user_id             ,
            "show_avatars"                  : show_avatars               ,
            "send_notifications_to_email"   : send_notifications_to_email,
            "bot_account"                   : bot_account                ,
            "show_bot_accounts"             : show_bot_accounts          ,
            "show_read_posts"               : show_read_posts            ,
            "show_new_post_notifs"          : show_new_post_notifs       ,
            "discussion_languages"          : discussion_languages       ,
            "generate_totp_2fa"             : generate_totp_2fa          
            }
        res = self._req.lemmyRequest("saveUserSettings", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def changePassword(self, 
        new_password: str,
        new_password_verify: str,
        old_password: str,
        instance:str=None,
        auth_token:str=None):
        form = {
            "new_password": new_password,
            "new_password_verify" : new_password_verify,
            "old_password": old_password
        }
        res = self._req.lemmyRequest("changePassword", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def getReportCount(self,community_id:int=None,  instance:str=None, auth_token:str=None):
        form={}
        optional={
            "community_id": community_id
            }
        res = self._req.lemmyRequest("getReportCount", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def getUnreadCount(self, instance:str=None, auth_token:str=None):
        form={}
        res = self._req.lemmyRequest("getUnreadCount", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def verifyEmail(self, instance:str=None, token:str=None):
        form={ "token": token }
        res = self._req.lemmyRequest("verifyEmail", instance=instance, form=form, auth=False, auth_token=auth_token)
        return res