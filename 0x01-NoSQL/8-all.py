#!/usr/bin/env python3
"""A script that lists all documents in a collection
"""


def list_all(mongo_collection):
    """mongo_collection: a pymango collection object
    """
    all_docs = mongo_collection.find()
    return all_docs
