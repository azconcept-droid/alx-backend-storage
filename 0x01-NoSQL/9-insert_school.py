#!/usr/bin/env python3
""" Module that insert new documents in collections
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection
    based on kwargs Returns the new _id
    """
    return mongo_collection.insert(kwargs)
