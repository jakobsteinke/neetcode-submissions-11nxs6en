class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # starting at index i what is LIS?
        memo = {}
        
        def dfs(i, last_num):
            if i == len(nums):
                return 0
            if (i, last_num) in memo:
                return memo[(i, last_num)]
            include = 0
            if nums[i] > last_num:
                include = 1 + dfs(i + 1, nums[i])
            not_include = dfs(i + 1, last_num)
            result = max(include, not_include)
            memo[(i, last_num)] = result
            return result
        return dfs(0, -math.inf)