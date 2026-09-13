class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        minElem = math.inf
        while l < r:
            m = l + (r - l)//2
            # which half is sorted?
            if nums[m] < nums[r]: # right half is sorted
                r = m - 1
            else: # left half is sorted
                l = m + 1
            minElem = min(min(min(minElem, nums[m]), nums[l]), nums[r])
        return minElem



