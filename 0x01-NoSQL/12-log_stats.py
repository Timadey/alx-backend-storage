#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient()
    nginx = client.logs.nginx
    print(f"""{nginx.count_documents({})} logs\nMethods:
    method GET: {nginx.count_documents({'method': 'GET'})}
    method POST: {nginx.count_documents({'method': 'POST'})}
    method PUT: {nginx.count_documents({'method': 'PUT'})}
    method PATCH: {nginx.count_documents({'method': 'PATCH'})}
    method DELETE: {nginx.count_documents({'method': 'DELETE'})}
{nginx.count_documents({'path': '/status'})} status check""")
