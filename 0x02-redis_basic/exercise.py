#!/usr/bin/env python3
"""
Module for exercises relating to REDIS Basics
"""
import redis
from typing import Union
import uuid


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
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, store the input date in Redis using
        the random key and return the key
        """
        key = uuid.uuid4()
        self._redis.set(key, data)
        return key
