#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound

from user import User


def _hash_password(password: str) -> str:
    """hash password method return bytes"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user method"""
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pass = _hash_password(password)
            return self._db.add_user(email, hashed_pass)

    def valid_login(self, email: str, password: str) -> bool:
        """valid the login user"""
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists is not None:
                hsd = user_exists.hashed_password
                if bcrypt.checkpw(password.encode('utf8'), hsd):
                    return True
            return False
        except NoResultFound:
            return False
