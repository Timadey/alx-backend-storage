#!/usr/bin/env python3
"""
A script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs\nMethods:")
    print(f"\tmethod GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(
        f"\tmethod DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    print(f"{nginx.count_documents({'path': '/status'})} status check")

    # Top 10 of the most present IPs in the nginx logs collection
    top10 = nginx.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {"$limit": 10}
    ])
    print("IPs:")
    for ip in top10:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
