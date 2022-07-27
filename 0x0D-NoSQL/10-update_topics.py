#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """change all topics of a school doc"""
    return mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})


if __name__ == "__main__":
    update_topics(mongo_collection, name, topics)
