class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, robFirst):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return 0 if robFirst else nums[i]

            if i in memo:
                return memo[i]
            if i == 0:
                memo[i] = nums[0] + dfs(i + 2, robFirst) if robFirst else dfs(i + 1, robFirst)  
            else:
                memo[i] = max(
                    nums[i] + dfs(i + 2, robFirst),  # rob
                    dfs(i + 1, robFirst)             # skip
                )

            return memo[i]

        robFirst = dfs(0, True)
        memo.clear()
        noRobFirst = dfs(0, False)
        return max(robFirst, noRobFirst)