class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(start, cur, sum):
            if sum > target:
                return
            if sum == target:
                result.append(cur)
                return
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i, cur.copy(), sum + nums[i])
                cur.pop()
        dfs(0, [], 0,)
        return result
