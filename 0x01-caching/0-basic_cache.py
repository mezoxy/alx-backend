#!/usr/bin/env python3
'''0-basic_cache.py'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache defines:
        - Caching system
    '''
    def put(self, key, item):
        '''
            put: A methode that assign an item to the dic self.cache_data
            Args:
                key: The key of the item
                item: The item to add in self.cache_data
        '''
        if key and item:
            self.cache_data[key] = item

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
