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
