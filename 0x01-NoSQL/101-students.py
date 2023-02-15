#!/usr/bin/env python3
"""
Function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Compute the average score of students on each topic and set a new
    field `averageScore in the document`
    mongo_collection: a pymongo collection object
    """
    result = mongo_collection.aggregate([
        {
            '$set': {
                'averageScore': {'$avg': '$topics.score'}
            }
        }, {
            '$sort': {'averageScore': -1}
        }
    ])
    return result
