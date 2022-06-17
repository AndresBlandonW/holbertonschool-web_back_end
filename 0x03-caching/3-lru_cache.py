#!/usr/bin/env python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Inherits from BaseCaching"""
    def __init__(self):
        """Initialize LRU Class"""
        self.LRUDict = {}
        super().__init__()

    def put(self, key, item):
        """Assign key: item to self.cache_data"""
        keyList = list(self.cache_data)[0:]
        if key and item:
            if key in keyList:
                del self.cache_data[key]
                keyList.remove(key)
                del self.LRUDict[key]
                self.LRUDict.update({key: 0})

            if key not in self.LRUDict:
                self.LRUDict.update({key: 0})

            keyList.append(key)

            if len(keyList) > self.MAX_ITEMS:
                del self.cache_data[keyList[0]]
                del self.LRUDict[keyList[0]]
                poppedKey = keyList.pop(0)
                print(f"DISCARD: {poppedKey}")

            self.cache_data.update({key: item})
            self.LRUDict.update({key: 0})

    def get(self, key):
        """Returns the value of self.cache_data of given key"""
        if key in self.LRUDict:
            value = self.LRUDict.pop(key)
            self.LRUDict.update({key: value + 1})

        self.__updateCache()
        return self.cache_data.get(key)

    def __updateCache(self):
        """Update cache_data Dict"""
        keys = list(self.LRUDict)[0:]
        values = [self.cache_data[k] for k in keys]
        newDict = {}
        for (k, v) in zip(keys, values):
            newDict[k] = v

        self.cache_data = newDict
