class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # each call: position
        # remaining push pop
        result = []
        def dfs(cur, remaining):
            if not remaining:
                result.append(cur.copy())
            for i in range(len(remaining)):
                r = remaining[i]
                cur.append(r)
                remaining.pop(i)
                dfs(cur, remaining)
                cur.pop()
                remaining.insert(i, r)
        dfs([], nums)
        return result


