#!/usr/bin/env python3
"""password module"""
import bcrypt


def _hash_password(password: str) -> str:
    """hash password method return bytes"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
    return hashed