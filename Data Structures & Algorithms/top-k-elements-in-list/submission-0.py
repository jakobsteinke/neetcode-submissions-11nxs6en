class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # each frequency can only be max of n 
        n = len(nums)
        freq = [[] for _ in range(n + 1)]
        counter = Counter(nums)
        for num, count in counter.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if len(res) == k:
                break
            res.extend(freq[i])
        
        return res
            
