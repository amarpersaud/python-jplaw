from .requestor import Requestor, HttpType
from .api_paths import *
from typing import List

class User():
    def __init__(self, _req: Requestor):
        self._req = _req
    def leaveAdmin(self, instance:str=None, auth_token:str=None):
        form = {}
        res = self._req.lemmyRequest(HttpType.POST, "leaveAdmin", instance=instance, form=form, auth=True, auth_token=auth_token))
    def register(self, username:str, password:str, password_verify:str, show_nsfw:bool, email:str=None, captcha_uuid:str=None, captcha_answer:str=None, honeypot:str=None, answer:str=None):
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
        form = _req.AddListIfValue(optional, form)
        res = self._req.lemmyRequest(HttpType.POST, "register", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    def getPersonDetails(self, instance:str=None, person_id:str=None, username:str=None, sort:str=None, page:int=0, limit:int=10, community_id:int=None, saved_only:bool=None, auth:bool=True, auth_token:str=None):
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
        form = _req.AddListIfValue(optional, form)
        res = self._req.lemmyRequest(HttpType.GET, "getPersonDetails", instance=instance, form=form, auth=auth, auth_token=auth_token))
        return res
    
    def markPersonMentionAsRead(self, instance:str=None, person_mention_id:int, read:bool=True, auth_token:str=None):
        form={
            "person_mention_id": person_mention_id,
            "read": read
        }
        res = self._req.lemmyRequest(HttpType.POST, "markPersonMentionAsRead", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def getPersonMentions(self, instance:str=None, sort:str=None, page:int=0, limit:int=10, unread_only:bool=True, auth_token:str=None):
        form={}
        optional = {
            "sort"           :sort           ,
            "page"           :page           ,
            "limit"          :limit          ,
            "unread_only"    :unread_only    ,
        }
        form=_req.AddListIfValue(optional, form)
        res = self._req.lemmyRequest(HttpType.GET, "getPersonMentions", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def getReplies(self, instance:str=None, sort:str=None, page:int=0, limit:int=10, unread_only:bool=True, auth_token:str=None):
        form={}
        optional = {
            "sort"           :sort           ,
            "page"           :page           ,
            "limit"          :limit          ,
            "unread_only"    :unread_only    ,
        }
        form=_req.AddListIfValue(optional, form)
        res = self._req.lemmyRequest(HttpType.GET, "getReplies", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def banPerson(self, person_id:int, ban:bool, remove_data:bool=None, reason:str=None, expires:int=None, auth_token:str=None):
        form={
            "person_id"     :person_id,
            "ban"           :ban
        }
        optional = {
            "remove_data"    :remove_data   ,
            "reason"         :reason        ,
            "expires"        :expires
        }
        form=_req.AddListIfValue(optional, form)
        res = self._req.lemmyRequest(HttpType.POST, "banPerson", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def getBannedPersons(self, instance:str=None, auth_token:str=None):
        form={}
        res = self._req.lemmyRequest(HttpType.GET, "getBannedPersons", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
     
    def blockPerson(self, person_id:int, block:bool, instance:str=None, auth_token:str=None):
        form={
            "person_id": person_id,
            "block": block
        }
        res = self._req.lemmyRequest(HttpType.POST, "blockPerson", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def getCaptcha(self, instance:str=None, auth_token:str=None):
        form={}
        res = self._req.lemmyRequest(HttpType.GET, "getCaptcha", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def deleteAccount(self, password, instance:str=None, auth_token:str=None):
        form={
            "password": password
        }
        res = self._req.lemmyRequest(HttpType.POST, "deleteAccount", instance=instance, form=form, auth=True, auth_token=auth_token))
        return res
    
    def passwordReset(self, email, instance:str=None, auth_token:str=None):
        form={
            "email": email
        }
        res = self._req.lemmyRequest(HttpType.POST, "passwordReset", instance=instance, form=form, auth=False, auth_token=auth_token))
        return res
    def passwordChangeAfterReset(self, token:str, password:str, password_verify:str):
        form={
            "token": token,
            "password": password,
            "password_verify": password_verify
        }
        res = self._req.lemmyRequest(HttpType.POST, "passwordChangeAfterReset", instance=instance, form=form, auth=False, auth_token=auth_token))
        return res
    def markAllAsRead(self, instance=None, community_view:str=None, site:str=None, moderators:List[str]=None, discussion_languages:List[str]=None)
        form={}
        optional={
            "community_view": community_view,
            "site": site,
            "moderators": moderators,
            "discussion_languages": discussion_languages,
        }
        form= self._req.AddListIfValue(optional, form)
        res = self._req.lemmyRequest(HttpType.POST, "passwordChangeAfterReset", instance=instance, form=form, auth=False, auth_token=auth_token))
        return res
