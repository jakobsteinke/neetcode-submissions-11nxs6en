class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(cur, remaining):
            if not remaining:
                result.append(cur)
                return
            for n in remaining: 
                cur.append(n)
                remaining.remove(n)
                dfs(cur.copy(), remaining.copy())
                cur.pop()
                remaining.add(n)

        dfs([], set(nums))
        return result


