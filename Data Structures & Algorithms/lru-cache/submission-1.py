class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # reinsert
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val


    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            firstInsertedKey = next(iter(self.cache))
            del self.cache[firstInsertedKey]
        elif key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        
