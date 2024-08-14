#!/usr/bin/env python3
""" Redis exercise module
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(fn: Callable) -> Callable:
    """ count how many calls """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """wrapper"""
        return fn(redis.Redis(), **kwargs)
    return wrapper


class Cache:
    """ Cache class
    """

    def __init__(self):
        """Initialize Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[bytes, str, int, float]) -> str:
        """store the input data in Redis using
        the random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        self.store.__qualname__ = key

        return key

    @count_calls
    def get(self, key: str,
            fn: Callable = None) -> Union[str, int, bytes, float]:
        """Get the value of a key in Redis"""
        data = self._redis.get(key)
        if data is None:
            return None

        if type(data) is bytes:
            return data

        if fn is int:
            self.get_int(data)

        if fn is str:
            self.get_str(data)

    def get_str(self, data):
        """ Get string data """
        if type(data) is str:
            return data.decode('utf-8')

    def get_int(self, data):
        """ Get int data """
        if type(data) in int:
            return int(data)
