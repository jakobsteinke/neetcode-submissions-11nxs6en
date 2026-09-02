class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        counter = defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            counter[s[r]] += 1
            maxChar = max(counter, key=counter.get)
            remainingK = (r - l + 1) - counter[maxChar]
            if remainingK <= k:
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                counter[s[l]] -= 1
                counter[s[r]] -= 1
                l += 1
        return maxLen