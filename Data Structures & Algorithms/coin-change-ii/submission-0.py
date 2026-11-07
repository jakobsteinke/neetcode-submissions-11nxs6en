class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # cur_am dp 
        mem = {}

        def dfs(cur_am, idx):
            if cur_am > amount or idx >= len(coins):
                return 0
            if cur_am == amount:
                return 1
            if (cur_am, idx) in mem:
                return mem[(cur_am, idx)]
            res = dfs(cur_am + coins[idx], idx) + dfs(cur_am, idx + 1)
            mem[(cur_am, idx)] = res
            return res
        
        return dfs(0, 0)