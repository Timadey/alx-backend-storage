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
    """ Decortator for counting """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper for decorator """
        red.incr(f"count:{url}")
        cached_html = red.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        red.setex(f"cached:{url}", 10, html)
        return html

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
