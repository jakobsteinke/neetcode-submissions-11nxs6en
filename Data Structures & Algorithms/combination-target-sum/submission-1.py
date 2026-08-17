class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(cur, sum, i):
            if sum == target:
                result.append(cur)
                return
            if sum > target or i == len(nums):
                return
            for j in range(i, len(nums)):
                num = nums[j]
                cur.append(num)
                sum += num
                dfs(cur.copy(), sum, j)
                cur.pop()
                sum -= num
        
        dfs([], 0, 0)
        return result