class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = defaultdict(int)

        for i in range(len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[len(nums) - 1]
