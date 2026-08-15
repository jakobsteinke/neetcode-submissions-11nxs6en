class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [
            (-math.sqrt(x**2 + y**2), [x, y])
            for x, y in points[:k]
        ]

        heapq.heapify(heap)

        for x, y in points[k:]:
            heapq.heappushpop(heap, (-math.sqrt(x**2 + y**2), [x, y]))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result