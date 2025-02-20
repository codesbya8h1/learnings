# Design and implement a data structure for the Least Recently Used (LRU) cache that supports the following operations:

# LRUCache(capacity: int): Initialize an LRU cache with the specified capacity.
# get(key: int) -> int: Return the value associated with a key. Return -1 if the key doesn't exist.
# put(key: int, value: int) -> None: Add a key and its value to the cache. If adding the key would result in the cache exceeding its size capacity, evict the least recently used element. If the key already exists in the cache, update its value.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def display(self):
        print(self.cache)

    def put(self, key, value):
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1


cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)

print(cache.get(1))
# cache.put(4, 4)
        
