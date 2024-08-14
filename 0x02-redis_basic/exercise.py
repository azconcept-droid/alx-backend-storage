#!/usr/bin/env python3
""" Redis exercise module
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Cache class
    """

    def __init__(self):
        """Initialize Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """store the input data in Redis using
        the random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None):
        """Get the value of a key in Redis"""

        return None
