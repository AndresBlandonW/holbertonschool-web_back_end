#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total = collection.count_documents({})
    get = collection.count_documents({'method': 'GET'})
    post = collection.count_documents({'method': 'POST'})
    put = collection.count_documents({'method': 'PUT'})
    patch = collection.count_documents({'method': 'PATCH'})
    delete = collection.count_documents({'method': 'DELETE'})
    status = collection.count_documents({'method': 'GET', 'path': '/status'})
    nl = '\n'

    print(f"{total} logs{nl}\
Methods:{nl}\
\tmethod GET: {get}{nl}\
\tmethod POST: {post}{nl}\
\tmethod PUT: {put}{nl}\
\tmethod PATCH: {patch}{nl}\
\tmethod DELETE: {delete}{nl}\
{status} status check")
