#!/usr/bin/env python3
"""
Module for exercises relating to REDIS Basics
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times methods
    of the Cache class are called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self._redis.incr(method.__qualname__)
        return result
    return wrapper


class Cache():
    """
    Cache class
    """

    def __init__(self) -> None:
        """
        Create and store an innstance of the Redis client
        Flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, store the input date in Redis using
        the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, None]:
        """
        Get a value from Redis with the given key
        """
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """
        Automiatically parametrize Cache.get with str conversion function
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Automiatically parametrize Cache.get with int conversion function
        """
        return self.get(key, int)
