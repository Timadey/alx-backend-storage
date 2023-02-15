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


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs of a particular
    function each time it is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function
    """
    rediss = redis.Redis()
    name = method.__qualname__
    count = rediss.get(name)
    inputs = rediss.lrange(f'{name}:inputs', 0, -1)
    outputs = rediss.lrange(f'{name}:outputs', 0, -1)
    print(f"{name} was called {count.decode('utf-8')} times:")

    for input, output in zip(inputs, outputs):
        print(f"{name}(*{input.decode('utf-8')}) -> {output.decode('utf-8')}")


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

    @call_history
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
