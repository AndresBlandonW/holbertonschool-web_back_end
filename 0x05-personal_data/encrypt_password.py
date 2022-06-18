#!/usr/bin/env python3
"""Hash password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password as a byte string"""
    password = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return True if matches, Flase otherwise"""
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
