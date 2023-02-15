#!/usr/bin/env python3
"""
Count how many times a web page is visited
"""
import requests
import redis
from typing import Callable
from functools import wraps


def count(method: Callable) -> Callable:
    """
    Count how many times a web page was visited
    """
    @wraps(method)
    def wrapper(*args):
        url = args[0]
        response = method(*args)
        if response.status_code == 200:
            red = redis.Redis()
            red.incr(f"count:{url}")
            red.expire(f"count:{url}", 10)
        return response.text
    return wrapper


@count
def get_page(url: str) -> str:
    """
    Obtains the HTML content of URL and returns it
    """
    return requests.get(url)

