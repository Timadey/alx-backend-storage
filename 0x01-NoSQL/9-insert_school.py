#!/usr/bin/env python3
"""Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """mongo_collection: a pymongo collection object
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
