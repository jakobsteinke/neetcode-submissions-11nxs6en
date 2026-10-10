class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # (index, sum1)
        summ_all = sum(nums)
        dp = {}

        def dfs(index, sum1):
            if (index, sum1) in dp:
                return dp[(index, sum1)]
            if index == len(nums):
                return sum1 == summ_all - sum1
            res = dfs(index + 1, sum1 + nums[index]) or dfs(index + 1, sum1)
            dp[(index, sum1)] = res
            return res
        
        return dfs(0, 0)