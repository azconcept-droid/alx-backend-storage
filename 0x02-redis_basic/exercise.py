#!/usr/bin/env python3
""" Redis exercise module
"""
import redis
import uuid
from typing import Any


class Cache:
    """ Cache class
    """

    def __init__(self):
        """Initialize Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Store method taht store key in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
