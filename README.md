# Python Lemmy API Wrapper
[![Build](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-package.yml)   [![PYPI Package](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/amarpersaud/python-jplaw/actions/workflows/python-publish.yml)
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
