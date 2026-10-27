class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        nums[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            max_reach = i
            for j in range(i + 1, min(n, i + 1 + nums[i])):
                max_reach = max(max_reach, nums[j])
            nums[i] = max_reach
        return nums[0] == n - 1