from .requestor import Requestor
from .api_paths import *


class PrivateMessage():
    def __init__(self, _req: Requestor):
        self._req = _req
        
    