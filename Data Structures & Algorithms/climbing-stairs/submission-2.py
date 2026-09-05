class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(cur, prev, prevprev):
            if cur == n:
                return prev
            return dfs(cur + 1, prev + prevprev, prev)

        return dfs(1, 1, 1)
