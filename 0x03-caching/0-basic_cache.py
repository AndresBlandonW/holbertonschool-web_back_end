#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching"""

    def put(self, key, item):
        """
            Assign key: item to self.cache_data
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """
            Returns the value of self.cache_data of given key
        """
        return self.cache_data.get(key)
