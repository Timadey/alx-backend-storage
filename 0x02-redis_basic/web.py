#!/usr/bin/env python3
"""
Count how many times a web page is visited
"""
import requests
import redis
from typing import Callable
from functools import wraps

red = redis.Redis()


def count(method: Callable) -> Callable:
    """
    Count how many times a web page was visited
    """
    @wraps(method)
    def wrapper(url):
        try:
            cached = red.get(f"cached:{url}")
            if cached:
                red.incr(f"count:{url}")
                return cached.decode('utf-8')
            res = method(url)
            red.incr(f"count:{url}")
            red.setex(f"cached:{url}", 10, res)
            return res
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
    return page.text
