class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # (index, profit, has_coin)
        # at each index decide if we want to buy

        mem = {}

        def dfs(index, profit, has_coin):
            if index >= len(prices):
                return profit
            if (index, has_coin) in mem:
                return profit + mem[(index, has_coin)]
            res = 0
            if not has_coin:
                res = max(dfs(index + 1, -prices[index], True), dfs(index + 1, 0, False))
            else:
                res = max(dfs(index + 2, prices[index], False), dfs(index + 1, 0, True))
            mem[(index, has_coin)] = res
            return res + profit
        
        return dfs(0, 0, False)