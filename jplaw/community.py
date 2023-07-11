"""
Community class. Designed to allow Lemmy.Community functions.
"""
from .requestor import Requestor
from .api_paths import *
from typing import List
from .types.listing_type import ListingType
from .types.sort_type import SortType

class Community():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    def get(self, name:str, instance:str=None, auth:bool=True):
        """
        Get community information
        
        Args:
            name (str): Name of the community. Federated communities can be accessed by [community]@[instance] 
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (str): If true, authenticates using internal token from login. Optional. Default True
        Returns:
            Community Information. Throws an error if community_not_found (happens if community has not been federated or does not exist)
        """
        form = {
            "name": name
        }
        res = self._req.lemmyRequest("getCommunity", instance=instance, form=form, auth=auth)
        return res["community_view"]
        
    def list(self, 
        type: ListingType=None, 
        sort:SortType=None,
        show_nsfw: bool=None,
        page:int=None, 
        limit:int=None, 
        instance:str=None, 
        auth:bool=True): 
        """
        Get a list of communities (federated or local)
        
        Args:
            type (ListingType): Type of community (all or local). Optional
            sort (SortType): Sorting Mode. Optional
            show_nsfw (bool): Whether or not to show nsfw communities. Optional. 
            page (int): Page number. Optional
            limit (int): Limit for number of posts. Optional
            instance (str): URL of local instance. Optional. Default None uses logged in instance
            auth (str): If true, authenticates using internal token from login. Optional. Default True
        Returns:
            List of communities
        """
        form={}
        optional={
            "sort"      : sort,
            "type"      : type,
            "show_nsfw" : show_nsfw,
            "page"      : page,
            "limit"     : limit
            }
        res = self._req.lemmyRequest("listCommunities", instance=instance, form=form, optional=optional, auth=auth)
        return res["communities"]
        
    def follow(self, community_id:int, follow:bool=True, instance:str=None):
        """
        Follow or subscribe to a community
        
        Args:
            community_id (int): ID of the community
            follow (bool): If true, subscribed to or following the community. Optional. Defaults to True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            List of communities
        """
        form={
            "community_id": community_id,
            "follow": follow
        }
        res = self._req.lemmyRequest("followCommunity", instance=instance, form=form, auth=True)
        return res["community_view"]
    def addMod(self, community_id:int, person_id:int, added:bool=True, instance:str=None): 
        """
        Add or remove a moderator from a community
        
        Args:
            community_id (int): ID of the community
            person_id (int): User ID of the person to add as a moderator
            added (bool): If true, person is added as a moderator. If false, person is removed as a moderator. Optonal. Default True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Added moderator response
        """
        form={
            "community_id": community_id,
            "person_id": person_id,
            "added": added,
        }
        res = self._req.lemmyRequest("addModToCommunity", instance=instance, form=form, auth=True)
        return res
    
    def banPerson(self, community_id:int, person_id:int, ban:bool, remove_data:bool=None, reason:str=None, expires:int=None, instance:str=None):
        """
        Ban a person from a community
        
        Args:
            community_id (int): ID of the community
            person_id (int): User ID of the person to ban
            ban (bool): If true, person is banned. If false, person is unbanned Optonal. Default True
            remove_data (bool): ??? Presumably removes the user's posts and comments or removes their data from the instance. Optional.
            reason (str): Reason for banning user. Optional
            expires (int): Unix timestamp of ban expiry (seconds)
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Banned community response
        """
        form={
            "community_id": community_id,
            "person_id": person_id,
            "ban": ban,
        }
        optional={
            "remove_data": remove_data,
            "reason": reason,
            "expires": expires,
        }
        res = self._req.lemmyRequest("banFromCommunity", instance=instance, form=form, optional=optional, auth=True)
        return res
        
    def block(self, community_id:int, block:bool=True, instance:str=None):
        """
        Block a community
        
        Args:
            community_id (int): ID of the community
            ban (bool): If true, community blocked. If false, community is unblocked. Optonal. Default True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Blocked community response
        """
        form={
            "community_id": community_id,
            "block": block,
            }
        res = self._req.lemmyRequest("blockCommunity", instance=instance, form=form, auth=True)
        return res["community_view"]
        
    def create(self, name:str, 
        title:str, 
        description:str=None, 
        icon:str=None, 
        banner:str=None, 
        nsfw:bool=None, 
        posting_restricted_to_mods:bool=None, 
        discussion_languages:List[int]=None, 
        instance:str=None):
        """
        Create a community
        
        Args:
            name (str): Name of the community
            title (str): Title of the community. Can have spaces.
            description (str): Description of the community. Optional.
            icon (str): URL of the community icon. Optional.
            banner (str): URL of the community banner image. Optional.
            nsfw (bool): If true, community is NSFW. Optional.
            posting_restricted_to_mods (bool): If true, only moderators can post. Optional.
            discussion_languages (List[int]): List of langages in community. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Created community response
        """
        form={
            "name": name,
            "title": title,
            }
        optional={
            "description": description,
            "icon": icon,
            "banner": banner,
            "nsfw": nsfw,
            "posting_restricted_to_mods": posting_restricted_to_mods,
            "discussion_languages": discussion_languages,
            }
        res = self._req.lemmyRequest("createCommunity", instance=instance, form=form, optional=optional, auth=True)
        return res["community_view"]
        
    def delete(self, community_id:int, deleted:bool=True, instance:str=None):
        """
        Delete a community
        
        Args:
            community_id (int): ID of the community
            deleted (bool): If true, community is deleted. If false, community is not deleted. Optonal. Default True
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Deleted community response
        """
        form={
            "community_id": community_id,
            "deleted": deleted,
            }
        res = self._req.lemmyRequest("deleteCommunity", instance=instance, form=form, auth=True)
        return res["community_view"]
    
    def edit(self, 
        community_id:int, 
        title:str=None, 
        description:str=None, 
        icon:str=None, 
        banner:str=None, 
        nsfw:bool=None, 
        posting_restricted_to_mods:bool=None, 
        discussion_languages:List[int]=None, 
        instance:str=None):
        """
        Edit a community. Excluding optional items does not edit those items.
        
        Args:
            community_id (int): ID of the community to edit
            title (str): Title of the community. Can have spaces. Optional
            description (str): Description of the community. Optional.
            icon (str): URL of the community icon. Optional.
            banner (str): URL of the community banner image. Optional.
            nsfw (bool): If true, community is NSFW. Optional.
            posting_restricted_to_mods (bool): If true, only moderators can post. Optional.
            discussion_languages (List[int]): List of langages in community. Optional.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Edited community response
        """
        form={
            "community_id": community_id,
            }
        optional={
            "title": title,
            "description": description,
            "icon": icon,
            "banner": banner,
            "nsfw": nsfw,
            "posting_restricted_to_mods": posting_restricted_to_mods,
            "discussion_languages": discussion_languages,
            }
        res = self._req.lemmyRequest("editCommunity", instance=instance, form=form, optional=optional, auth=True)
        return res["community_view"]
        
    def remove(self, community_id:int, removed:bool=True, reason:str=None, expires:int=None, instance:str=None):
        """
        Remove a community
        
        Args:
            community_id (int): ID of the community
            removed (bool): If true, community is removed. If false, community is restored. Optonal. Default True
            reason (str): Reason for community removal. Optional.
            expires (int): Unix timestamp (seconds) of expiry.
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Removed community response
        """
        form={
            "community_id": community_id,
            "removed":removed,
            }
        optional={
            "reason": reason,
            "expires": expires,
            }
        res = self._req.lemmyRequest("removeCommunity", instance=instance, form=form, optional=optional, auth=True)
        return res["community_view"]
    
    def transfer(self, community_id:int, person_id:int, instance:str=None):
        """
        Transfer ownership of a community
        
        Args:
            community_id (int): ID of the community
            person_id (int): User ID of the person to transfer ownership to
            instance (str): URL of local instance. Optional. Default None uses logged in instance
        Returns:
            Removed community response
        """
        form={
            "community_id": community_id,
            "person_id":person_id,
            }
        res = self._req.lemmyRequest("transferCommunity", instance=instance, form=form, auth=True)
        return res["community_view"]
