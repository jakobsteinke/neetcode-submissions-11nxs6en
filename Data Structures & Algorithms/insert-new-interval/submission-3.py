from bisect import bisect_right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        # intervals before our interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # curInterval[1] >= newInteval[0]:
        while i < len(intervals) and (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][0] or
        newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][1] or 
        newInterval[0] >= intervals[i][0] and newInterval[1] <= intervals[i][1]):
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        result.append(newInterval)
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result



        