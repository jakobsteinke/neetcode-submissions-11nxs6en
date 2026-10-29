class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                res = 1
                if j + 1 < n:
                    res = dp[i][j + 1]
                if i + 1 < m:
                    res = dp[i + 1][j]
                if j + 1 < n and i + 1 < m:
                    res = dp[i][j + 1] + dp[i + 1][j]
                dp[i][j] = res
        return dp[0][0]
