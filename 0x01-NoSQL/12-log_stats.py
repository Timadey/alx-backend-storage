#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient()
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs\nMethods:")
    print(f"\tmethod GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(
        f"\tmethod DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    print(f"{nginx.count_documents({'path': '/status'})} status check")
