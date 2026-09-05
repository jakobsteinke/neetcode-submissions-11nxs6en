class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        fastDict = Counter(wordDict)
        memo = {}

        def dfs(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if r > len(s) and l < len(s):
                return False
            if l >= len(s):
                return True
            sol = False
            if s[l:r] in fastDict:
                sol = dfs(r, r + 1) or dfs(l, r + 1)
            else: 
                sol = dfs(l, r + 1)
            memo[(l, r)] = sol
            return sol

        return dfs(0, 0)
