class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(i, cur):
            if i >= len(nums):
                result.append(cur)
                return
            cur.append(nums[i])
            dfs(i + 1, cur.copy())
            cur.pop()
            dfs(i + 1, cur.copy())
            return
        dfs(0, [])
        return result
