#!/usr/bin/env python3
# Retrieve values from a nested object

def get_value(obj, search_key):
    """Get value of a search_key from input object.

    Keyword arguments:
    obj -- input object
    search_key -- Key, whose value is to be retrieved 
    """
    for key in obj:
        if key == search_key:
            return obj.get(key)
        elif isinstance(obj.get(key), dict):
            return get_value(obj.get(key), search_key)
