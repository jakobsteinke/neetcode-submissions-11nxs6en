class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-2 for _ in range(amount + 1)]
        memo[0] = 0
        for coin in coins:
            if coin <= amount:
                memo[coin] = 1

        def dfs(amount):
            if memo[amount] != -2:
                return memo[amount]
            minCoins = -1
            for coin in coins:
                if coin <= amount:
                    testCoin = dfs(amount - coin)
                    if testCoin != -1:
                        testCoin += 1
                        minCoins = testCoin if minCoins == -1 else min(minCoins, testCoin)
            memo[amount] = minCoins
            return minCoins

        return dfs(amount)