class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # stay and pick
        # or dont pick and move

        res = []

        def dfs(cur, i, s):
            if s == target:
                res.append(cur.copy())
                return
            if s > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(cur, i, s + nums[i])
            cur.pop()
            dfs(cur, i + 1, s)

        dfs([], 0, 0)
        return res
