#!/usr/bin/env python3
"""list of collection with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list of school"""
    return mongo_collection.find({'topics': topic})


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
