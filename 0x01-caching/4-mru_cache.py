#!/usr/bin/env python3
'''4-mru_cache.py'''


from base_caching import BaseCaching
from datetime import datetime


class MRUCache(BaseCaching):
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
                k = [
                    i for i in self.__curDate.keys()
                    if self.__curDate[i] == max(
                            self.__curDate.values())
                        ][0]
                if key in self.cache_data.keys():
                    self.cache_data[key] = item
                else:
                    print(f'DISCARD: {k}')
                    del self.cache_data[k]
                    del self.__curDate[k]
                    self.cache_data[key] = item
                self.__curDate[key] = datetime.now()

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
