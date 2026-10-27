class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # if we dont choose, skip all
        # when choose, then + 1
        candidates.sort()
        res = []
        def dfs(cur, i, s):
            if s == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or s > target:
                return
            
            cur.append(candidates[i])
            dfs(cur, i + 1, s + candidates[i])
            cur.pop()
            i += 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
                i += 1
            dfs(cur, i, s)

        dfs([], 0, 0)
        return res