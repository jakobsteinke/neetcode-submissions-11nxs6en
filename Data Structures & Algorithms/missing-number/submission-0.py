class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        for n in nums:
            sum1 += n
        sum2 = 0
        for n in range(len(nums) + 1):
            sum2 += n
        return sum2 - sum1