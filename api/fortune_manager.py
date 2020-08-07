"""A module for managing the list of fortunes data saved in
the Python memory.

This is where we put the function helpers for managing the fortunes data.
"""
import random

from api import cache


def load_fortunes(filepath="api/data/cookie_sayings2.txt"):
    """Load the text file into a list of strings and save to the cache."""
    text_file = open(filepath, 'r')
    lines = text_file.read().split("\n")[:-1]
    text_file.close

    cache.put("fortunes", lines)
    return lines


def get_fortune():
    """Picks a random fortune based on the list saved."""
    fortunes = cache.get("fortunes")
    return random.choice(fortunes)


def update_fortune(old_fortune, new_fortune):
    """Replaces a fortune with an updated fortune from the user.

    TODO: This algorithm has a lot of steps and I'm sure there's an
    updated algorithm somewhere that is faster than this.
    """
    # Get the list of fortunes in the cache
    fortunes = cache.get("fortunes")

    # Look and replace the fortune.
    # TODO: Dangerous assumption that text is clean from the request body
    # and front-end. A better way to do this is to usea better matching
    # algorithm.
    updated_fortunes = [new_fortune if f == old_fortune else f for f
            in fortunes]

    # Save the updated list of fortunes in the cache.
    cache.update("fortunes", updated_fortunes)
    return new_fortune
