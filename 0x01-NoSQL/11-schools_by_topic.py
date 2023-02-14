#!/usr/bin/env python3
"""List of schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection: a pymongo collection object
    topic: (string) the topic searched
    """
    return mongo_collection.find({'topics': topic})
