#!/usr/bin/env python3
"""FIFO caching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching"""

    def put(self, key, item):
        """Assign key: item to self.cache_data"""
        keyList = list(self.cache_data)[0:]
        if key and item:
            if key in keyList:
                del self.cache_data[key]
                keyList.remove(key)

            keyList.append(key)

            if len(keyList) > BaseCaching.MAX_ITEMS:
                del self.cache_data[keyList[0]]
                poppedKey = keyList.pop(0)
                print(f"DISCARD: {poppedKey}")

            self.cache_data.update({key: item})

    def get(self, key):
        """Returns the value of self.cache_data of given key"""
        return self.cache_data.get(key)
