class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        distToLastAdj = 1
        for i in range(length - 2, -1, -1):
            if nums[i] < distToLastAdj:
                distToLastAdj += 1
            else:
                distToLastAdj = 1
        return distToLastAdj == 1