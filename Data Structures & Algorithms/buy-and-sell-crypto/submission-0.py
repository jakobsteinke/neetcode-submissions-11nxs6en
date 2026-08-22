class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestGain = 0
        bestMin = prices[0]
        for price in prices:
            bestGain = max(bestGain, price - bestMin)
            bestMin = min(bestMin, price)
        return bestGain