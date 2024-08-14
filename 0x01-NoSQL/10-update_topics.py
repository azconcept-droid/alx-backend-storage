#!/usr/bin/env python3
""" Module update all topics
"""


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics of a school document
    based on the name
    """
    mongo_collection.update({ 'name': name }, {'topics': topics })
