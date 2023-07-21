"""
User class. Designed to allow Lemmy.User functions.
"""
from .requestor import Requestor
from .api_paths import *
from typing import List
from .types.listing_type import ListingType
from .types.sort_type import SortType

class User():
    def __init__(self, _req: Requestor):
        self._req = _req
    def leaveAdmin(self, instance:str=None):
        """
        Leave the administrator team of a site
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Removed community response
        """
        form = {}
        res = self._req.lemmyRequest("leaveAdmin", instance=instance, form=form, auth=True)
    def register(self, 
        username:str, 
        password:str, 
        password_verify:str, 
        show_nsfw:bool, 
        email:str=None, 
        captcha_uuid:str=None, 
        captcha_answer:str=None, 
        honeypot:str=None, 
        answer:str=None, 
        instance:str=None):
        """
        Register at an instance
        
        Args:
            username (str): Username to use for account
            password (str): Password for account
            password_verify (str): Password repeated for verification
            show_nsfw (bool): If NSFW posts should be shown
            email (str): Email address associated with the account. Optional
            captcha_uuid (str): UUID of the captcha. Optional. Required if site requires captcha.
            captcha_answer (str): Answer to the captcha. Optional. Required if site requires captcha.
            honeypot (str): Honeypot field. Used for detecting bots which autofill all fields. Do not use unless trying to explicitly trigger honeypot
            answer (str): Answer to sign up question
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Removed community response
        """
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
        res = self._req.lemmyRequest("register", instance=instance, form=form, optional=optional, auth=False)
        return res
    def getDetails(self, person_id:str=None, username:str=None, sort:SortType=None, page:int=None, limit:int=None, community_id:int=None, saved_only:bool=None, instance:str=None, auth:bool=True):
        """
        Get details of a user
        
        Args:
            person_id (int): User ID of the person to get the details of. Optional.
            username (str): Username of the user to get the details of. Optional
            sort (SortType): Sort order of user list. Optional
            page (int): Page number to get.
            limit (int): Limit for number of users to return
            community_id (int): Community to filter by for user
            saved_only (bool): Show only saved objects
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (bool): If true, authenticate using login. Defaults to True.
            
        Returns:
            List of items which follow the filters given
        """
        form={}
        optional={
            "sort"          :   sort              ,
            "person_id"     :   person_id         ,
            "username"      :   username          ,
            "page"          :   page              ,
            "limit"         :   limit             ,
            "community_id"  :   community_id      ,
            "saved_only"    :   saved_only        ,
            }
        res = self._req.lemmyRequest("getPersonDetails", instance=instance, form=form, optional=optional, auth=auth)
        return res
    
    def markMentionAsRead(self, person_mention_id:int, read:bool=True, instance:str=None):
        """
        Mark a mention as read or unread
        
        Args:
            person_mention_id (int): ID of the mention
            read (bool): If true, marks mention as read. False marks unread. Defaults to True. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of items which follow the filters given
        """
        form={
            "person_mention_id": person_mention_id,
            "read": read
            }
        res = self._req.lemmyRequest("markPersonMentionAsRead", instance=instance, form=form, auth=True)
        return res
    
    def getMentions(self, sort:SortType=None, page:int=None, limit:int=None, unread_only:bool=True, instance:str=None):
        """
        Get the list of mentions
        
        Args:
            sort (SortType): Sort order of mention list. Optional
            page (int): Page number to get. Optional.
            limit (int): Limit for number of mentions to return. Optional.
            unread_only (bool): Show only unread mentions. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of mentions
        """
        form={}
        optional = {
            "sort"           :  sort           ,
            "page"           :  page           ,
            "limit"          :  limit          ,
            "unread_only"    :  unread_only    ,
            }
        res = self._req.lemmyRequest("getPersonMentions", instance=instance, form=form, optional=optional, auth=True)
        return res
    
    def getReplies(self, sort:SortType=None, page:int=None, limit:int=None, unread_only:bool=True):
        """
        Get the list of replies
        
        Args:
            sort (SortType): Sort order of reply list. Optional
            page (int): Page number to get. Optional.
            limit (int): Limit for number of replies to return. Optional.
            unread_only (bool): Show only unread replies. Optional. Defaults to true.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of replies
        """
        form={}
        optional = {
            "sort"           :  sort           ,
            "page"           :  page           ,
            "limit"          :  limit          ,
            "unread_only"    :  unread_only    ,
            }
        res = self._req.lemmyRequest("getReplies", instance=instance, form=form, optional=optional, auth=True)
        return res
    
    def ban(self, person_id:int, ban:bool, remove_data:bool=None, reason:str=None, expires:int=None, instance:str=None):
        """
        Ban a user from the instance
        
        Args:
            person_id (int): User ID of the person to ban
            ban (bool): If the user is banned from the instance.
            remove_data (bool): Remove the data of the user. Optional.
            expires (int): Unix Timestamp of ban expiration (seconds). Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Banned user 
        """
        form={
            "person_id"     :person_id,
            "ban"           :ban
            }
        optional = {
            "remove_data"    :remove_data   ,
            "reason"         :reason        ,
            "expires"        :expires
            }
        res = self._req.lemmyRequest("banPerson", instance=instance, form=form, optional=optional, auth=True)
        return res
    
    def getBanned(self, instance:str=None):
        """
        Get the list of banned users
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            List of banned users
        """
        form={}
        res = self._req.lemmyRequest(HttpType.GET, "getBannedPersons", instance=instance, form=form, auth=True)
        return res
     
    def block(self, person_id:int, block:bool, instance:str=None):
        """"
        Block or unblock a user
        
        Args:
            person_id (int): ID of the user to block
            block (bool): True to block user. False to unblock user. 
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Blocked user response
        """
        form={
            "person_id": person_id,
            "block": block
            }
        res = self._req.lemmyRequest("blockPerson", instance=instance, form=form, auth=True)
        return res
    
    def getCaptcha(self, instance:str=None): 
        """
        Get a new captcha from an instance
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Captcha
        """
        form={}
        res = self._req.lemmyRequest("getCaptcha", instance=instance, form=form, auth=True)
        return res
    
    def deleteAccount(self, password:str, instance:str=None): 
        """
        Delete an account
        
        Args:
            password (str): password to verify account deletion
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Deleted account response
        """
        form={
            "password": password
            }
        res = self._req.lemmyRequest("deleteAccount", instance=instance, form=form, auth=True)
        return res
    
    def passwordReset(self, email:str, instance:str=None): 
        """
        Reset an account password associated with an email
        
        Args:
            email (str): Email address an account is associated with
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Pasword reset response
        """
        form={
            "email": email
            }
        res = self._req.lemmyRequest("passwordReset", instance=instance, form=form, auth=False)
        return res
        
    def passwordChangeAfterReset(self, token:str, password:str, password_verify:str, instance:str=None):
        """
        Change a password after reset request
        
        Args:
            token (str): Reset token sent to email address
            password (str): New password
            password_verify (str): New password repeated for verification
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Password reset response
        """
        form={
            "token": token,
            "password": password,
            "password_verify": password_verify
            }
        res = self._req.lemmyRequest("passwordChangeAfterReset", instance=instance, form=form, auth=False)
        return res
        
    def markAllAsRead(self, instance:str=None):
        """
        Mark all as read
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Mark read response
        """
        form={}
        res = self._req.lemmyRequest("markAllAsRead", instance=instance, form=form, auth=True)
        return res
        
    def saveUserSettings(self,
        show_nsfw: bool=None,
        blur_nsfw: bool=None,
        auto_expand: bool=None,
        show_scores: bool=None,
        theme: str=None,
        default_sort_type: SortType=None,
        default_listing_type: ListingType=None,
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
        discussion_languages: List[int]=None, 
        generate_totp_2fa: bool=None, 
        open_links_in_new_tab: bool=None,
        instance:str=None):
        """
        Save user settings to account
        
        Args:
            show_nsfw (bool): If NSFW posts and communities should be shown. Optional
            show_scores (bool): If scores should be shown. Optional
            blur_nsfw (bool): If nsfw thumbnails and images should be blurred before opening the image. Optional
            auto_expand (bool): If true, autoexpand images. Optional.
            theme (str): Site theme. Optional
            default_sort_type (SortType): Sort type for the site. Optional
            default_listing_type (ListingType): Default listing type. Allows viewing Local or All communities. Optional
            interface_language (str): Interface language string. Optional
            avatar (str): URL of avatar. Optional
            banner (str): URL of user banner. Optional
            display_name (str): DIsplay name of the user. Optional
            email (str): Email address associated with the account. Optional
            bio (str): User Bio/Description. Optional
            matrix_user_id (str): Matrix user ID. Optional
            show_avatars (bool): If user avatars should be shown next to names. Optional 
            send_notifications_to_email (bool): If email notifications should be sent to the user. Optional
            bot_account (bool): If this is a bot account. Optional
            show_bot_accounts (bool): If bot accounts should be hidden. Optional 
            show_read_posts (bool): If read posts should be shown or hidden . Optional
            show_new_post_notifs (bool): If new posts should send a notification. Optional
            discussion_languages (List[int]): List of langages to show. Using undefined may cause no posts to show. Optional
            generate_totp_2fa (bool): Use TOTP 2FA. Optional
            open_links_in_new_tab (bool): Open links in new tab. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            User settings saved response
        """ 
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
            "generate_totp_2fa"             : generate_totp_2fa          ,
            "open_links_in_new_tab"         : open_links_in_new_tab
            }
        res = self._req.lemmyRequest("saveUserSettings", instance=instance, form=form, optional=optional, auth=True)
        return res
    def changePassword(self, 
        new_password: str,
        new_password_verify: str,
        old_password: str,
        instance:str=None):
        """
        Change password
        
        Args:
            new_password (str): New password
            new_password_verify (str): New password repeated for verification
            old_password (str): Old password to verify identity
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Password changed response
        """
        form = {
            "new_password": new_password,
            "new_password_verify" : new_password_verify,
            "old_password": old_password
        }
        res = self._req.lemmyRequest("changePassword", instance=instance, form=form, auth=True)
        return res
        
    def getReportCount(self,community_id:int=None, instance:str=None):
        """
        Get the report count
        
        Args:
            community_id (int): ID of the community. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Report count response
        """
        form={}
        optional={
            "community_id": community_id
            }
        res = self._req.lemmyRequest("getReportCount", instance=instance, form=form, optional=optional, auth=True)
        return res
        
    def getUnreadCount(self, instance:str=None):
        """
        Get the unread count
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            
        Returns:
            Unread count response
        """
        form={}
        res = self._req.lemmyRequest("getUnreadCount", instance=instance, form=form, auth=True)
        return res
        
    def verifyEmail(self, instance:str=None, token:str=None):
        """
        Verify an email address
        
        Args:
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            token (str): Authentication token from email
        Returns:
            Password changed response
        """
        form={ "token": token }
        res = self._req.lemmyRequest("verifyEmail", instance=instance, form=form, auth=False)
        return res
