class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # (idx, cur_sum)

        memo = {}

        def dfs(idx, cur_sum):
            if idx > len(nums):
                return 0
            if cur_sum == target and idx == len(nums):
                return 1
            if idx == len(nums):
                return 0
            if (idx, cur_sum) in memo:
                return memo[(idx, cur_sum)]
            
            res = dfs(idx + 1, cur_sum - nums[idx]) + dfs(idx + 1, cur_sum + nums[idx])

            memo[(idx, cur_sum)] = res

            return res

        return dfs(0, 0)