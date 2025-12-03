#!/usr/bin/env python3
"""
Module for updating document topics in MongoDB collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates topics of all school documents with specific name

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list): list of topics approached in the school

    Returns:
        UpdateResult: result of the update operation
    """
    fil = {"name": name}
    update = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(fil, update)
    return result
