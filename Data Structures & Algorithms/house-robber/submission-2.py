class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        # rob or not rob
        def dfs(robbedLast, house):
            if (robbedLast, house) in memo:
                return memo[(robbedLast, house)]
            if house == len(nums):
                return 0
            solution = 0
            if robbedLast:
                solution =  dfs(False, house + 1)
            else: 
                solution = max(nums[house] + dfs(True, house + 1), dfs(False, house + 1))
            memo[(robbedLast, house)] = solution
            return solution
        return dfs(False, 0)
