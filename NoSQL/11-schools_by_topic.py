#!/usr/bin/env python3
"""
Module for finding schools by specific topic in MongoDB collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for in schools

    Returns:
        Cursor: pymongo cursor with schools that have the specified topic
    """
    search = {"topics": topic}
    result = mongo_collection.find(search)
    return result
