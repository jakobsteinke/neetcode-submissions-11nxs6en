class TimeMap:

    def __init__(self):
        self.storage = {} #by key, inside lists sorted by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = [(value, timestamp)]
        else:
            self.storage[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        # binary search
        slot = self.storage[key]
        closestValue = ""
        l, r = 0, len(slot) - 1
        while l <= r:
            m = l + (r - l) // 2
            if slot[m][1] > timestamp:
                r = m - 1
            elif slot[m][1] < timestamp:
                l = m + 1
                closestValue = slot[m][0]
            else: 
                return slot[m][0]
        return closestValue






