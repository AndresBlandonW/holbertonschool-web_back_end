#!/usr/bin/env python3
"""Insert in collection Pymongo"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document"""
    return mongo_collection.insert(kwargs)


if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
