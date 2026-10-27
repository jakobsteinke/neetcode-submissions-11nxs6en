class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if cur overlaps with prev, remove the one with the bigger end
        min_removes = 0
        intervals.sort(key=lambda x:x[0])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if prev_end > cur[0]:
                prev_end = min(prev_end, cur[1])
                min_removes += 1
            else:
                prev_end = cur[1]
        return min_removes
        