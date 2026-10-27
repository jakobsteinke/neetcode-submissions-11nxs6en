class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 2 3 4 
        # 1, max(piles)
        # time_needed -> for pile in piles: time_needed += math.ceil(pile/rate)

        l, r = 1, max(piles)
        while l <= r:
            rate = l + (r - l) // 2
            time_needed = 0
            for pile in piles:
                time_needed += math.ceil(pile/rate)
            if time_needed > h:
                l = rate + 1
            else:
                r = rate - 1
        return l
