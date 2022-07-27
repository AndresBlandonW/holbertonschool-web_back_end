#!/usr/bin/env python3
"""List all documents mongodb"""


def list_all(mongo_collection):
    """list collection"""
    return mongo_collection.find() or []


if __name__ == "__main__":
    list_all(mongo_collection)
