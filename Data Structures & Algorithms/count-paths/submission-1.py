class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res = 0
                if j + 1 < n:
                    res += dp[i][j + 1]
                if i + 1 < m:
                    res += dp[i + 1][j]
                if j + 1 < n and i + 1 < m:
                    res += 1
                dp[i][j] = res
        return dp[0][0] + 1
