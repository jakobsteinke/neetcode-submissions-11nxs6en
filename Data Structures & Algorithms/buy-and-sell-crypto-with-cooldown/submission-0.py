class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # (index, profit, has_coin)
        # at each index decide if we want to buy

        mem = {}

        def dfs(index, profit, has_coin):
            if index >= len(prices):
                return profit
            if (index, profit, has_coin) in mem:
                return mem[(index, profit, has_coin)]
            res = 0
            if not has_coin:
                res = max(dfs(index + 1, profit - prices[index], True), dfs(index + 1, profit, False))
            else:
                res = max(dfs(index + 2, profit + prices[index], False), dfs(index + 1, profit, True))
            mem[(index, profit, has_coin)] = res
            return res
        
        return dfs(0, 0, False)