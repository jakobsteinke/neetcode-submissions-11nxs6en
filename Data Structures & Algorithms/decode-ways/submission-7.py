class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        
        def dfs(index):
            if index >= len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]
            res = dfs(index + 1)
            if index + 1 < len(s):
                if int(s[index]) == 1 or int(s[index]) == 2 and int(s[index + 1]) <= 6:
                    res += dfs(index + 2)
            memo[index] = res
            return res
        
        return dfs(0)