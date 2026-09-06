class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        def dfs(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            sol = 0
            if text1[i1] == text2[i2]:
                sol =  1 + dfs(i1 + 1, i2 + 1)
            else: sol = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            memo[(i1, i2)] = sol
            return sol

        return dfs(0, 0)         
