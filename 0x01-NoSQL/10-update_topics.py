"""function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """mongo_collection: a pymango collection object
    name: (string) the schol name to update
    topics: (list of strings) the list of topics approached in the school
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
