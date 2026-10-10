class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n * log k)
        # am ende k größten elemente im min heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]