from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # key -> list((timestamp, value))
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        value_list = self.map[key]
        # find the first timestamp > our timestamp
        # 2 2 3 4 4 4 4 4
        index = bisect_right(value_list, timestamp, key=lambda x:x[0]) - 1
        if index == -1:
            return ""
        return value_list[index][1]



        
