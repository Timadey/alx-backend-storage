#!/usr/bin/env python3
"""
Count how many times a web page is visited
"""
import requests
import redis
from typing import Callable
from functools import wraps

red = redis.Redis()


def count_visits(method: Callable) -> Callable:
    """
    Count how many times a web page was visited
    """
    @wraps(method)
    def wrapper(url):
        cached = red.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        res = method(url)
        red.incr(f"count:{url}")
        red.set(f"cached:{url}", res)
        red.expire(f"cached:{url}", 10)
        return res
    return wrapper


@count_visits
def get_page(url: str) -> str:
    """
    Obtains the HTML content of URL and returns it
    """
    page = requests.get(url)
    return page.text
