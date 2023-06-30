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
        """
        Get the site details
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (bool): Whether or not to authenticate. Optional. Defaults to True.
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Instance details response
        """
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
        """
        Create the lemmy instance
        
        Args:
            name (str): Name of the website                 
            sidebar (str): Text of the sidebar of the website. Optional.
            description (str): Description of the website. Optional.
            icon (str): URL to icon for webstite. Optional.
            banner (str): URL for banner of website. Optional.
            enable_downvotes (bool): If true, downvotes are enabled. Optional.
            enable_nsfw (bool): If true, NSFW content is allowed. Optional.
            community_creation_admin_only (bool): If true, only adminstrators can create communities. Optional.
            require_email_verification (bool): If true, email verification is required. Optional.
            application_question (str): Question shown on application. Optional.
            private_instance (bool): If true, instance is private. Optional.
            default_theme (str): Default theme for the site. Optional.
            default_post_listing_type (ListingType): Default listing type for posts. Optional.
            legal_information (str): Legal information for the site. Optional.
            application_email_admins (bool): If applications send an email to the admins. Optional.
            hide_modlog_mod_names (bool): If true, moderator names are hidden in the modlog. Optional.
            discussion_languages (List[int]): List of discussion languages in the instance. Optional.
            slur_filter_regex (str): Regex to match for slurs or to block certain text. 
            actor_name_max_length (int): Maximum name length for actors ???. Optional. 
            rate_limit_message (int): Message rate limit. Optional.
            rate_limit_message_per_second (int): Message per second rate limit. Optional.
            rate_limit_post (int): Post rate limit. Optional.
            rate_limit_post_per_second (int): Post per second rate limit. Optional.
            rate_limit_register (int): Registration rate limit. Optional.
            rate_limit_register_per_second (int): Registrations per second rate limit. Optional.
            rate_limit_image (int): Image rate limit. Optional.
            rate_limit_image_per_second (int): Image rate limit per second. Optional.
            rate_limit_comment (int): Comment rate limit. Optional.
            rate_limit_comment_per_second (int): Comment per second rate limit. Optional.
            rate_limit_search (int): Search rate limit. Optional.
            rate_limit_search_per_second (int): Search per second rate limit. Optional.
            federation_enabled (bool): If federation is enabled. Optional.
            federation_debug (bool): If federation debugging is enabled. Optional.
            federation_worker_count (int): Number of federation workers. This is the number of threads dedicated to federating content. Optional.
            captcha_enabled (bool): If captcha is enabled. Optional.
            captcha_difficulty (str): Difficulty of the captcha. Text: easy, medium or hard.
            allowed_instances (List[str]): List of allowed instances. Optional.
            blocked_instances (List[str]: List of blocked or defederated instances. Optional.
            taglines (List[str]: List of taglines shown at top of front page). Optional.
            registration_mode (RegistrationMode): Mode of registration (Closed/Application/Open). Optional.
            reports_email_admins (bool): if reporting emails the admins. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Create site response
        """
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
        name: str=None,
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
        """
        Edit the site details. Optional arguments can be excluded to leave them as is.
        
        Args:
            name (str): Name of the website. Optional            
            sidebar (str): Text of the sidebar of the website. Optional.
            description (str): Description of the website. Optional.
            icon (str): URL to icon for webstite. Optional.
            banner (str): URL for banner of website. Optional.
            enable_downvotes (bool): If true, downvotes are enabled. Optional.
            enable_nsfw (bool): If true, NSFW content is allowed. Optional.
            community_creation_admin_only (bool): If true, only adminstrators can create communities. Optional.
            require_email_verification (bool): If true, email verification is required. Optional.
            application_question (str): Question shown on application. Optional.
            private_instance (bool): If true, instance is private. Optional.
            default_theme (str): Default theme for the site. Optional.
            default_post_listing_type (ListingType): Default listing type for posts. Optional.
            legal_information (str): Legal information for the site. Optional.
            application_email_admins (bool): If applications send an email to the admins. Optional.
            hide_modlog_mod_names (bool): If true, moderator names are hidden in the modlog. Optional.
            discussion_languages (List[int]): List of discussion languages in the instance. Optional.
            slur_filter_regex (str): Regex to match for slurs or to block certain text. 
            actor_name_max_length (int): Maximum name length for actors ???. Optional. 
            rate_limit_message (int): Message rate limit. Optional.
            rate_limit_message_per_second (int): Message per second rate limit. Optional.
            rate_limit_post (int): Post rate limit. Optional.
            rate_limit_post_per_second (int): Post per second rate limit. Optional.
            rate_limit_register (int): Registration rate limit. Optional.
            rate_limit_register_per_second (int): Registrations per second rate limit. Optional.
            rate_limit_image (int): Image rate limit. Optional.
            rate_limit_image_per_second (int): Image rate limit per second. Optional.
            rate_limit_comment (int): Comment rate limit. Optional.
            rate_limit_comment_per_second (int): Comment per second rate limit. Optional.
            rate_limit_search (int): Search rate limit. Optional.
            rate_limit_search_per_second (int): Search per second rate limit. Optional.
            federation_enabled (bool): If federation is enabled. Optional.
            federation_debug (bool): If federation debugging is enabled. Optional.
            federation_worker_count (int): Number of federation workers. This is the number of threads dedicated to federating content. Optional.
            captcha_enabled (bool): If captcha is enabled. Optional.
            captcha_difficulty (str): Difficulty of the captcha. Text: easy, medium or hard.
            allowed_instances (List[str]): List of allowed instances. Optional.
            blocked_instances (List[str]: List of blocked or defederated instances. Optional.
            taglines (List[str]: List of taglines shown at top of front page). Optional.
            registration_mode (RegistrationMode): Mode of registration (Closed/Application/Open). Optional.
            reports_email_admins (bool): if reporting emails the admins. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Edit site response
        """
        form = {}
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
        """
        Get the list of federated instances from the site
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (bool): Whether or not to use authentication. Optional. Defaults to True.
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Federated instances response
        """
        res = self._req.lemmyRequest("getFederatedInstances", instance=instance, auth=auth, auth_token=auth_token)
        return res
        
    def createCustomEmoji(self, category:str, shortcode:str, image_url:str, alt_text:str, keywords:List[str], instance:str=None, auth_token:str=None):
        """
        Create a custom emoji
        
        Args:
            category (str): Category of the emoji
            shortcode (str): Short code used to type the emoji
            image_url (str): URL of the image to use
            alt_text (str): Alt text (hover or screenreader) of the emoji
            keywords (List[str]): Keywords of the emoji.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Emoji created response
        """
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
        """
        Edit a custom emoji. Excluded optional arguments are not modified.
        
        Args:
            emoji_id (int): ID of the emoji
            category (str): Category of the emoji. Optional
            image_url (str): URL of the image to use. Optional
            alt_text (str): Alt text (hover or screenreader) of the emoji. Optional
            keywords (List[str]): Keywords of the emoji. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Emoji edited response
        """
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
        """
        Delete a custom emoji from the website
        
        Args:
            emoji_id (int): ID of emoji to delete
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Emoji deleted response
        """
        form={
            "id": emoji_id
            }
        res = self._req.lemmyRequest("deleteCustomEmoji", instance=instance, form=form, auth=auth, auth_token=auth_token)
        return res

    def addAdmin(self, person_id:int, added:bool=True, instance:str=None, auth_token:str=None):
        """
        Add an administrator to the site
        
        Args:
            person_id (int): ID of user to add as administrator
            added (bool): If person is added as an administrator to the site. Optional. Defaults to True.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Administrator added response
        """
        form={
            "person_id": person_id,
            "added": added
            }
        res = self._req.lemmyRequest("addAdmin", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def getUnreadRegistrationApplicationCount(self, instance:str=None, auth_token=None):
        """
        Get the number of unread registration applications
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Unread registration application count response
        """
        form={}
        res = self._req.lemmyRequest("getUnreadRegistrationApplicationCount", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def listRegistrationApplications(self, unread_only:bool=None, page:int=None, limit:str=None, instance:str=None, auth_token=None):
        """
        Get a list of registration applications
        
        Args:
            unread_only (bool): Get only unread applications. Optional.
            page (int): Page of applications to get. Optional.
            limit (int): Limit for number of applications to get. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            List of registration applications 
        """
        form={}
        optional={
            "page": page,
            "limit": limit,
            "unread_only": unread_only
            }
        res = self._req.lemmyRequest("listRegistrationApplications", instance=instance, form=form, auth=True, auth_token=auth_token)
        return res
        
    def approveRegistrationApplication(self, application_id:int, approve:bool=True, deny_reason:str=None, instance:str=None, auth_token:str=None):
        """
        Approve a registration application
        
        Args:
            application_id (int): ID of the application
            approve (bool): If registration application has been approved. Optional. Defaults to True
            dent_reason (str): Reason for denying the application, if denied. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Approved registration response
        """
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
        """
        Get the moderation log of the site
        
        Args:
            mod_person_id (int): Filter by moderator id. Optional
            community_id (int): Filter by community id. Optional
            page (int): Page number to view. Optional
            limit (int): Limit for number of results to get. Optional
            type_ (ModlogActionType): Filter by type of moderator action. Optional
            other_person_id (int): ID of the user who made the comment, post or community. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Moderator log response
        """
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
        """
        Purge a comment from the site
        
        Args:
            comment_id (int): ID of the comment to purge
            reason (str): Reason for purging the comment. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Purged comment response
        """
        form={
            "comment_id": comment_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgeComment", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def purgeCommunity(self, community_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        """
        Purge a community from the site
        
        Args:
            community_id (int): ID of the user to purge
            reason (str): Reason for purging the community. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Purged community response
        """
        form={
            "community_id": community_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgeCommunity", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def purgePost(self, post_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        """
        Purge a post from the site
        
        Args:
            post_id (int): ID of the post to purge
            reason (str): Reason for purging the post. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Purged post response
        """
        form={
            "post_id": post_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgePost", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
    def purgePerson(self, person_id:int, reason:str=None, instance:str=None, auth_token:str=None):
        """
        Purge a person from the site
        
        Args:
            person_id (int): ID of the user to purge
            reason (str): Reason for purging the person. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth_token (str): Authentication token for local instance. Optional. Default None uses logged in auth_token
        Returns:
            Purged person response
        """
        form={
            "person_id": person_id
            }
        optional={
            "reason": reason,
            }
        res = self._req.lemmyRequest("purgePerson", instance=instance, form=form, optional=optional, auth=True, auth_token=auth_token)
        return res
