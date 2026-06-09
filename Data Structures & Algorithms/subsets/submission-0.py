class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(idx, cur):
            if idx >= len(nums):
                result.append(cur.copy())
                return
            cur.append(nums[idx])
            dfs(idx + 1, cur)
            cur.pop()
            dfs(idx + 1, cur)
        dfs(0, [])
        return result