#!/usr/bin/env python3
"""Session auth"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        sessionid = str(uuid.uuid4())
        self.user_id_by_session_id.update({sessionid: user_id})

        return sessionid

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)
