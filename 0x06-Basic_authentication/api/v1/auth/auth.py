#!/usr/bin/env python3
"""manage the API authentication"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method to auth"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path = path + '/'

        for rsl in excluded_paths:
            if rsl[-1] == '*':
                rsl = rsl[0:-1]

            if rsl in path:
                return False

        if path not in excluded_paths:
            return True

        return False


    def authorization_header(self, request=None) -> str:
        """method authorization header"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """method current user"""
        return request
