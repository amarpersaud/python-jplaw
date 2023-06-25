from .requestor import Requestor
from .api_paths import *
from typing import List
from .types.modlog_action_type import ModlogActionType
from .types.listing_type import ListingType
from .types.registration_mode import RegistrationMode

class Site():
    def __init__(self, _req: Requestor):
        self._req = _req
    
    def getSite(self, instance:str=None, auth:bool=True, auth_token:str=None):
        form = {}
        res = self._req.lemmyRequest("getSite", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
    
    def createSite(self,    
        name: str,
        sidebar: str=None,
        description: str=None,
        icon: str=None,
        banner: str=None,
        enable_downvotes: bool=None,
        enable_nsfw: bool=None,
        community_creation_admin_only: bool=None,
        require_email_verification: bool=None,
        application_question: str=None,
        private_instance: bool=None,
        default_theme: str=None,
        default_post_listing_type: ListingType=None,
        legal_information: str=None,
        application_email_admins: bool=None,
        hide_modlog_mod_names: bool=None,
        discussion_languages: List[int]=None,
        slur_filter_regex: str=None,
        actor_name_max_length: int=None,
        rate_limit_message: int=None,
        rate_limit_message_per_second: int=None,
        rate_limit_post: int=None,
        rate_limit_post_per_second: int=None,
        rate_limit_register: int=None,
        rate_limit_register_per_second: int=None,
        rate_limit_image: int=None,
        rate_limit_image_per_second: int=None,
        rate_limit_comment: int=None,
        rate_limit_comment_per_second: int=None,
        rate_limit_search: int=None,
        rate_limit_search_per_second: int=None,
        federation_enabled: bool=None,
        federation_debug: bool=None,
        federation_worker_count: int=None,
        captcha_enabled: bool=None,
        captcha_difficulty: str=None,
        allowed_instances: List[str]=None,
        blocked_instances: List[str]=None,
        taglines: List[str]=None,
        registration_mode: RegistrationMode=None,
        instance:str=None, 
        auth_token:str=None):
        form = {
            "name"                              : name                              ,
            }
        optional = {
            "sidebar"                           : sidebar                           ,
            "description"                       : description                       ,
            "icon"                              : icon                              ,
            "banner"                            : banner                            ,
            "enable_downvotes"                  : enable_downvotes                  ,
            "enable_nsfw"                       : enable_nsfw                       ,
            "community_creation_admin_only"     : community_creation_admin_only     ,
            "require_email_verification"        : require_email_verification        ,
            "application_question"              : application_question              ,
            "private_instance"                  : private_instance                  ,
            "default_theme"                     : default_theme                     ,
            "default_post_listing_type"         : default_post_listing_type         ,
            "legal_information"                 : legal_information                 ,
            "application_email_admins"          : application_email_admins          ,
            "hide_modlog_mod_names"             : hide_modlog_mod_names             ,
            "discussion_languages"              : discussion_languages              ,
            "slur_filter_regex"                 : slur_filter_regex                 ,
            "actor_name_max_length"             : actor_name_max_length             ,
            "rate_limit_message"                : rate_limit_message                ,
            "rate_limit_message_per_second"     : rate_limit_message_per_second     ,
            "rate_limit_post"                   : rate_limit_post                   ,
            "rate_limit_post_per_second"        : rate_limit_post_per_second        ,
            "rate_limit_register"               : rate_limit_register               ,
            "rate_limit_register_per_second"    : rate_limit_register_per_second    ,
            "rate_limit_image"                  : rate_limit_image                  ,
            "rate_limit_image_per_second"       : rate_limit_image_per_second       ,
            "rate_limit_comment"                : rate_limit_comment                ,
            "rate_limit_comment_per_second"     : rate_limit_comment_per_second     ,
            "rate_limit_search"                 : rate_limit_search                 ,
            "rate_limit_search_per_second"      : rate_limit_search_per_second      ,
            "federation_enabled"                : federation_enabled                ,
            "federation_debug"                  : federation_debug                  ,
            "federation_worker_count"           : federation_worker_count           ,
            "captcha_enabled"                   : captcha_enabled                   ,
            "captcha_difficulty"                : captcha_difficulty                ,
            "allowed_instances"                 : allowed_instances                 ,
            "blocked_instances"                 : blocked_instances                 ,
            "taglines"                          : taglines                          ,
            "registration_mode"                 : registration_mode                 ,
            }
        res = self._req.lemmyRequest("createSite", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    
    def editSite(self,         
        name: str,
        sidebar: str=None,
        description: str=None,
        icon: str=None,
        banner: str=None,
        enable_downvotes: bool=None,
        enable_nsfw: bool=None,
        community_creation_admin_only: bool=None,
        require_email_verification: bool=None,
        application_question: str=None,
        private_instance: bool=None,
        default_theme: str=None,
        default_post_listing_type: ListingType=None,
        legal_information: str=None,
        application_email_admins: bool=None,
        hide_modlog_mod_names: bool=None,
        discussion_languages: List[int]=None,
        slur_filter_regex: str=None,
        actor_name_max_length: int=None,
        rate_limit_message: int=None,
        rate_limit_message_per_second: int=None,
        rate_limit_post: int=None,
        rate_limit_post_per_second: int=None,
        rate_limit_register: int=None,
        rate_limit_register_per_second: int=None,
        rate_limit_image: int=None,
        rate_limit_image_per_second: int=None,
        rate_limit_comment: int=None,
        rate_limit_comment_per_second: int=None,
        rate_limit_search: int=None,
        rate_limit_search_per_second: int=None,
        federation_enabled: bool=None,
        federation_debug: bool=None,
        federation_worker_count: int=None,
        captcha_enabled: bool=None,
        captcha_difficulty: str=None,
        allowed_instances: List[str]=None,
        blocked_instances: List[str]=None,
        taglines: List[str]=None,
        registration_mode: RegistrationMode=None,
        reports_email_admins:bool=None,
        instance:str=None, 
        auth_token:str=None):
        form = {
            }
        optional = {
            "name"                              : name                              ,
            "sidebar"                           : sidebar                           ,
            "description"                       : description                       ,
            "icon"                              : icon                              ,
            "banner"                            : banner                            ,
            "enable_downvotes"                  : enable_downvotes                  ,
            "enable_nsfw"                       : enable_nsfw                       ,
            "community_creation_admin_only"     : community_creation_admin_only     ,
            "require_email_verification"        : require_email_verification        ,
            "application_question"              : application_question              ,
            "private_instance"                  : private_instance                  ,
            "default_theme"                     : default_theme                     ,
            "default_post_listing_type"         : default_post_listing_type         ,
            "legal_information"                 : legal_information                 ,
            "application_email_admins"          : application_email_admins          ,
            "hide_modlog_mod_names"             : hide_modlog_mod_names             ,
            "discussion_languages"              : discussion_languages              ,
            "slur_filter_regex"                 : slur_filter_regex                 ,
            "actor_name_max_length"             : actor_name_max_length             ,
            "rate_limit_message"                : rate_limit_message                ,
            "rate_limit_message_per_second"     : rate_limit_message_per_second     ,
            "rate_limit_post"                   : rate_limit_post                   ,
            "rate_limit_post_per_second"        : rate_limit_post_per_second        ,
            "rate_limit_register"               : rate_limit_register               ,
            "rate_limit_register_per_second"    : rate_limit_register_per_second    ,
            "rate_limit_image"                  : rate_limit_image                  ,
            "rate_limit_image_per_second"       : rate_limit_image_per_second       ,
            "rate_limit_comment"                : rate_limit_comment                ,
            "rate_limit_comment_per_second"     : rate_limit_comment_per_second     ,
            "rate_limit_search"                 : rate_limit_search                 ,
            "rate_limit_search_per_second"      : rate_limit_search_per_second      ,
            "federation_enabled"                : federation_enabled                ,
            "federation_debug"                  : federation_debug                  ,
            "federation_worker_count"           : federation_worker_count           ,
            "captcha_enabled"                   : captcha_enabled                   ,
            "captcha_difficulty"                : captcha_difficulty                ,
            "allowed_instances"                 : allowed_instances                 ,
            "blocked_instances"                 : blocked_instances                 ,
            "taglines"                          : taglines                          ,
            "registration_mode"                 : registration_mode                 ,
            "reports_email_admins"              : reports_email_admins              ,
            }
        res = self._req.lemmyRequest("editSite", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def getFederatedInstances(self, instance:str=None, auth:bool=True, auth_token:str=None):
        res = self._req.lemmyRequest("getFederatedInstances", instance=instance, auth=auth, auth_token=auth_token)
        return res
        
    def createCustomEmoji(self, category:str, shortcode:str, image_url:str, alt_text:str, keywords:List[str], instance:str=None, auth_token:str=None):
        form={
            "category": category,
            "shortcode": shortcode,
            "image_url": image_url,
            "alt_text": alt_text,
            "keywords": keywords
            }
        res = self._req.lemmyRequest("createCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def editCustomEmoji(self, emoji_id:int, category:str=None, image_url:str=None, alt_text:str=None, keywords:List[str]=None, instance:str=None, auth_token:str=None):
        form={
            "id": emoji_id,
            "category": category,
            "image_url": image_url,
            "alt_text": alt_text,
            "keywords": keywords
            }
        res = self._req.lemmyRequest("editCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res
        
    def deleteCustomEmoji(self, emoji_id:int, instance:str=None, auth_token:str=None):
        form={
            "id": emoji_id
            }
        res = self._req.lemmyRequest("deleteCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res

    def addAdmin(self, person_id:int, added:bool, instance:str=None, auth_token:str=None):
        form={
            "person_id": person_id,
            "added": added
            }
        res = self._req.lemmyRequest("addAdmin", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def getUnreadRegistrationApplicationCount(self, instance:str=None, auth_token=None):
        form={}
        res = self._req.lemmyRequest("getUnreadRegistrationApplicationCount", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def listRegistrationApplications(self, unread_only:bool=None, page:int=None, limit:str=None, instance:str=None, auth_token=None):
        form={}
        optional={
            "page": page,
            "limit": limit,
            "unread_only": unread_only
            }
        res = self._req.lemmyRequest("listRegistrationApplications", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def approveRegistrationApplication(self, application_id:int, approve:bool, deny_reason:str=None, instance:str=None, auth_token:str=None):
        form={
            "application_id": application_id,
            "approve": approve,
            }
        optional={
            "deny_reason": deny_reason
            }
        res = self._req.lemmyRequest("approveRegistrationApplication", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def getModlog(self, mod_person_id:int=None, community_id:int=None, page:int=None, limit:int=None, type_:ModlogActionType=None, other_person_id:int=None, instance:str=None, auth_token:str=None):
        form={}
        optional={
            "mod_person_id": mod_person_id,
            "community_id": community_id,
            "page": page,
            "limit": limit,
            "type_": type_,
            "other_person_id": other_person_id,
            }
        res = self._req.lemmyRequest("getModlog", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
        
    def purgeComment(self, comment_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        form={
            "comment_id": comment_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgeComment", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def purgeCommunity(self, community_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        form={
            "community_id": community_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgeCommunity", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def purgePost(self, post_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        form={
            "post_id": post_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgePost", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def purgePerson(self, person_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        form={
            "person_id": person_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgePerson", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res