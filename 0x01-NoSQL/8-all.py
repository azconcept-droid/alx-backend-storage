#!/usr/bin/env python3
""" Module that list all documents in collections
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
    """
    doc = []
    for x in mongo_collection.find():
        doc.append(x)

    return doc
