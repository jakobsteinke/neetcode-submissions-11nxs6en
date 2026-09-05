class Solution:
    def numDecodings(self, s: str) -> int:
        # memoization
        # f(i + 1) + f(i + 2)
        # if second one is 0, just f(i + 2)
        # if i + 1 is out of bounds: return 1 
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index == len(s) - 1:
                return 1
            sol = dfs(index + 1)
            if not (int(s[index]) == 2 and index + 1 < len(s) and int(s[index + 1]) > 6 or int(s[index]) > 2):
                sol += dfs(index + 2)
            memo[index] =  sol
            return memo[index]
            
        return dfs(0) 


        # analyze space and time 