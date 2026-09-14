class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # countOpen, countClosed
        # when countClosed < countOpen: closed possible
        # when countOpen < n: open possible
        # append when both counts = n 

        result = []
        def dfs(count_open, count_closed, cur):
            if count_open == n and count_closed == n:
                result.append(cur)
                return
            if count_open < n:
                cur += '('
                dfs(count_open + 1, count_closed, cur)
                cur = cur[:-1]
            if count_closed < count_open:
                cur += ')'
                dfs(count_open, count_closed + 1, cur)
        
        dfs(0, 0, "")
        return result
        