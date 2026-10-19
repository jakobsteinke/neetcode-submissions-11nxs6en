"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
       # heap of endtimes
       # pop heap while top.end <= cur.start 
       # put cur in heap
       # max is max(heap.size(), cur_max)
       heap = []
       intervals.sort(key=lambda x: (x.start, x.end))
       num_rooms = 0
       for interval in intervals:
        start = interval.start
        end = interval.end
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        num_rooms = max(num_rooms, len(heap))
       return num_rooms
