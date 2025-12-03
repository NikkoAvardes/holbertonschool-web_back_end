#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list: all documents in the collection, or empty list if no documents
    """
    return list(mongo_collection.find())
