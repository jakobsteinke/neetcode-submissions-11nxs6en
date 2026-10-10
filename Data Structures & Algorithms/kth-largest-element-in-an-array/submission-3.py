class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n * log k)
        # am ende k größten elemente im min heap
        heap = []
        for num in nums:
            if len(heap) == k:
                curMin = heapq.heappop(heap)
                if curMin < num:
                    heapq.heappush(heap, num)
                else:
                    heapq.heappush(heap, curMin)
            else:
                heapq.heappush(heap, num)
        return heap[0]