class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        memo[0] = 1
        memo[1] = 1
        def getResult(n):
            if memo[n] != -1:
                return memo[n]
            res = getResult(n - 1) + getResult(n - 2)
            memo[n] = res
            return res
        return getResult(n)