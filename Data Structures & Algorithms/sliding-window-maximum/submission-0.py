class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # counter for elements in window
        # heap with lazy evaluation
        heap = []
        counter = defaultdict(int)
        for i in range(k):
            heap.append(-nums[i])
            counter[nums[i]] += 1
        heapq.heapify(heap)
        res = [-heap[0]]

        l = 0
        for r in range(k, len(nums)):
            counter[nums[l]] -= 1
            l += 1
            heapq.heappush(heap, -nums[r])
            counter[nums[r]] += 1
            while heap and counter[-heap[0]] == 0:
                heapq.heappop(heap)
            res.append(-heap[0])
        return res