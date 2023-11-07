from flask import request
from typing import List, TypeVar


class Auth:
    """ classs to handle Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication
        return:
            -return Flase
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header to return None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Checks The current user and returns the object """
        return None
