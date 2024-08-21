#!/usr/bin/env python3
'''1-fifo_cache.py'''


from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    '''BasicCache defines:
        - Caching system
    '''
    __curDate = {}

    def put(self, key, item):
        '''
            put: A methode that assign an item to the dic self.cache_data
            Args:
                key: The key of the item
                item: The item to add in self.cache_data
        '''
        if key and item:
            if len(self.cache_data.keys()) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.__curDate[key] = datetime.now()
            else:
                # print(self.__curDate)
                # print('#' * 80)
                # print(self.cache_data)
                k = [i for i in self.__curDate.keys() if self.__curDate[i] == min(self.__curDate.values())][0]
                print(f'DISCARD: {k}')
                del self.cache_data[k]
                del self.__curDate[k]
                self.__curDate[key] = datetime.now()
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
                self.__curDate.update({key: datetime.now()})
                return self.cache_data[key]
        except Exception as e:
            return None
