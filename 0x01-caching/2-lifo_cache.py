#!/usr/bin/env python3
'''1-fifo_cache.py'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''BasicCache defines:
        - Caching system
    '''
    __pwd = None
 
    def put(self, key, item):
        '''
            put: A methode that assign an item to the dic self.cache_data
            Args:
                key: The key of the item
                item: The item to add in self.cache_data
        '''
        if key and item:
            if len(self.cache_data.keys()) < BaseCaching.MAX_ITEMS:
                self.__pwd = key
                self.cache_data[key] = item
            else:
                print(f'DISCARD: {self.__pwd}')
                del self.cache_data[self.__pwd]
                self.cache_data[key] = item
                self.__pwd = key

    def get(self, key):
        '''
            get: A method that retrive an item by key

            Args:
                key: The key of the item to retrive

            Return: The item if the key and the item are not None
        '''
        try:
            if key:
                return self.cache_data[key]
        except Exception as e:
            return None
