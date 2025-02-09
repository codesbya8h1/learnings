from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            # Move accessed item to end
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            # Update value and move to end
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used item (first item)
                self.cache.popitem(last=False)
        self.cache[key] = value

# Example Usage
cache = LRUCache(3)
cache.put(2, 2)
cache.put(1,5)
cache.put(4,6)
cache.put(3, 3)      
print(cache.get(2)) 