#!/usr/bin/env python3
"""LFU caching module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching algorithm"""
    __LFUDict = {}
    __bit = 0

    def put(self, key, item):
        """Assign key: item to self.cache_data"""
        keyList = list(self.cache_data)[0:]
        if key and item:
            if key in keyList:
                self.cache_data.update({key: item})
                self.__LFUDict.update({key: self.__bit})
                self.__bit += 1
            else:
                if len(self.cache_data) < self.MAX_ITEMS:
                    self.__LFUDict.update({key: self.__bit})
                    self.__bit += 1
                    self.cache_data.update({key: item})
                else:
                    discardedKey = self.__updateCache(key, item)
                    print(f"DISCARD: {discardedKey}")

    def get(self, key):
        """Returns the value of self.cache_data of given key"""
        keyList = list(self.cache_data)[0:]
        if key in keyList:
            self.__LFUDict[key] = self.__bit
            self.__bit += 1
        return self.cache_data.get(key)

    def __updateCache(self, key, item):
        """Update the cache dictionary"""
        keys = list(self.__LFUDict)[0:]
        values = [self.__LFUDict[k] for k in keys]
        cacheVals = [self.cache_data[k] for k in keys]

        minVal = min(values)
        index = values.index(minVal)
        minKey = keys[index]

        keys[index] = key
        values[index] = self.__bit - 1
        cacheVals[index] = item

        self.cache_data.clear()
        self.cache_data = {k: v for k, v in zip(keys, cacheVals)}

        self.__LFUDict.clear()
        self.__LFUDict = {k: v for k, v in zip(keys, values)}

        return minKey
