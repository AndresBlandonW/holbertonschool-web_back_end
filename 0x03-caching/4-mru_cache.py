#!/usr/bin/env python3
"""MRU caching module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Inherits from BaseCaching"""
    __MRUDict = {}
    __bit = 0

    def put(self, key, item):
        """Assign key: item to self.cache_data"""
        keyList = list(self.cache_data)[0:]
        if key and item:
            if key in keyList:
                self.cache_data.update({key: item})
                self.__MRUDict.update({key: self.__bit})
                self.__bit += 1
            else:
                if len(self.cache_data) < self.MAX_ITEMS:
                    self.__MRUDict.update({key: self.__bit})
                    self.__bit += 1
                    self.cache_data.update({key: item})
                else:
                    discardedKey = self.__updateCache(key, item)
                    print(f"DISCARD: {discardedKey}")

    def get(self, key):
        """Returns the value of self.cache_data of given key"""
        keyList = list(self.cache_data)[0:]
        if key in keyList:
            self.__MRUDict[key] = self.__bit
            self.__bit += 1
        return self.cache_data.get(key)

    def __updateCache(self, key, item):
        """Update the cache dictionary"""
        keys = list(self.__MRUDict)[0:]
        values = [self.__MRUDict[k] for k in keys]
        cacheVals = [self.cache_data[k] for k in keys]

        maxVal = max(values)
        index = values.index(maxVal)
        maxKey = keys[index]

        keys[index] = key
        values[index] = self.__bit - 1
        cacheVals[index] = item

        self.cache_data.clear()
        self.cache_data = {k: v for k, v in zip(keys, cacheVals)}

        self.__MRUDict.clear()
        self.__MRUDict = {k: v for k, v in zip(keys, values)}

        return maxKey
