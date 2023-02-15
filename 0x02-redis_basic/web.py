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
        try:
            url = args[0]
            res = method(*args)
            if res.status_code == 200:
                red = redis.Redis()
                red.incr(f"count:{url}")
                red.expire(f"count:{url}", 10)
            return res.text
        except TypeError:
            pass
    return wrapper


@count
def get_page(url: str) -> str:
    """
    Obtains the HTML content of URL and returns it
    """
    if type(url) != str:
        return TypeError("Url has to be a string")
    page = requests.get(url)
    return page
