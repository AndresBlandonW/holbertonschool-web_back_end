#!/usr/bin/env python3
"""Basic auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode, b64encode
from models.base import DATA
from models.user import User
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """Basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Basic - Base64 part"""
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if authorization_header[0:6] != 'Basic ':
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            return b64decode(base64_authorization_header,
                             None, True).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """
            returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) is not str:
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        auth_header = decoded_base64_authorization_header.split(':', 1)
        return (auth_header[0], auth_header[1])

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
            Returns the User instance based on his email and password
        """
        if user_email is None or type(user_email) is not str:
            return None

        if user_pwd is None or type(user_pwd) is not str:
            return None

        if DATA.get('User') is None:
            return None

        users = User.search({'email': user_email})
        if users is None:
            return None

        for user in users:
            if user.email == user_email and user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Overloads Auth and retrieves the User instance for a request
        """
        auth_header = super().authorization_header(request)
        if auth_header is not None:
            ah_extract = self.extract_base64_authorization_header(auth_header)
            ah_decode = self.decode_base64_authorization_header(ah_extract)
            email, password = self.extract_user_credentials(ah_decode)

            return self.user_object_from_credentials(email, password)

        return None
