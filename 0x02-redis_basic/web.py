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
        red = redis.Redis()
        red.incr(f"count:{args[0]}")
        red.expire(f"count:{args[0]}", 10)
        return method(*args)
    return wrapper


@count
def get_page(url: str) -> str:
    """
    Obtains the HTML content of URL and returns it
    """
    page = requests.get(url)
    return page.text
