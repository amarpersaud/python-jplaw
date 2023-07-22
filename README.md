# Python Lemmy API Wrapper
[![Build](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-package.yml) 
[![Generate Python Documentation](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-documentation.yml/badge.svg)](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-documentation.yml)

Like PRAW but for Lemmy

Written using the [Lemmy TS library](https://github.com/LemmyNet/lemmy-js-client) for reference.

Forked from benja810's plaw

Currently, most of the API functions are implemented, but there are likely quite a few bugs. It is a bit difficult to test at the moment without spinning up a new instance. 

If you find any bugs, let me know on the [issues page](https://github.com/amarpersaud/python-jplaw/issues)

# Installation
jplaw can be installed from PYPI through pip:

`python -m pip install jplaw`

# Usage example
This example uses python-dotenv to load secrets from the `.env` file, which is not strictly necessary.

```python
import jplaw
import dotenv

#Load secrets with dotenv
dotenv.load_dotenv()
my_instance = os.getenv("LEMMY_INSTANCE")
my_username = os.getenv("LEMMY_USERNAME")
my_password = os.getenv("LEMMY_PASSWORD")

lem = jplaw.Lemmy(my_instance, my_username, my_password)

#Print the JSON response from the community list
print(lem.Community.list())

#Print the JSON response from getting a specific community
print(lem.Community.get("test@lemmy.ml"))
```

# Documentation
See [the documentation](https://amarpersaud.github.io/python-jplaw/) for more information on how to use jplaw.

# Roadmap 
- Work on return types and usability.
- Work on testing functions and finding / squashing bugs

# Changelog
### v0.1.9
- Add blur_nsfw and auto_expand parameters to saveUserSettings
- Add moderator_view parameter to Post.list()

### v0.1.8
- Fixes Community.edit()
- Adds Lemmy.federateCommunity()


### v0.1.7
- Fix bug with "fixed" boolean values

### v0.1.6
- Fixes boolean and Enum parameters
- Adds show_nsfw to communities
- Add open_links_in_new_tab saveUserSettings
- Removes auth_token parameter from functions. To get an auth_token, a new Lemmy object can be created and logged in with. Accessing other instances via a Lemmy object can be done via the instance parameter, but does not authenticate
- Fix documentation for jplaw.types and jplaw.comment

### v0.1.5
- Fix namespace issues
- Fix build issues
- Fix missing instance argument in list communities

### v0.1.4
- Created documentation
    - Versioned documentation for browsing info on previous versions (things will prob change pretty quickly in early releases)
    - Available [here](https://amarpersaud.github.io/python-jplaw/)
- Fixed some issues with argument types not using enums properly or missing references
- Created Emoji class for creating, editing and deleting custom emoji

### v0.1.3
- Moved enums like SortType to submodule jplaw.types
- Fix missing enum types
- Rename a large portion of the functions to remove repetition.
    - Decouples naming scheme from Lemmy API
    - Shortens names and removes repetitive naming like "Lemmy.Comment.likeComment()" -> "Lemmy.Comment.like()."

### v0.1.2
- Added majority of the API functions except for image uploading

### v0.1.1
- Getting PyPi package working and added some functions

### v0.1
- Alpha release. After forking from plaw, fork was broken and migrated to this repository from the [jplaw](https://github.com/amarpersaud/jplaw/) repository, as I wanted to do something a little different from having a purely API equivalent library.
