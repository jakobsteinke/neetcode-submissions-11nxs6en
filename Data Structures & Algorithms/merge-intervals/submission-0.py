class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        j = 0
        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = result[j]
            if prev[1] >= cur[0]:
                result[j][1] = max(result[j][1], cur[1])
            else:
                j += 1
                result.append(cur)
        return result