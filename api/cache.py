"""Simple cache module to manage data in Python in-memory.

A better approach is to use a database.
"""

# Main cache dictionary
cache = {}


def put(key, value):
    cache[key] = value
    return cache


def get(key):
    return cache.get(key)


def update(key, value):
    cache[key] = value
    return cache
