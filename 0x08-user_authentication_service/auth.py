#!/usr/bin/env python3
"""auth module"""
import uuid
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound

from user import User


def _hash_password(password: str) -> str:
    """hash password method return bytes"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """generate a uuid"""
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """return a session id"""
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists is not None:
                session_id = _generate_uuid()
                self._db.update_user(user_exists.id, session_id=session_id)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """get user from session id method"""
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            if user is not None:
                return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session of user method"""
        self._db.update_user(user_id, session_id=None)
        return None
