class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # map to the last occurence of char, move l to max(l, lastOccurence), shift r 
        m = {}
        l = 0
        maxSubStr = 0
        for r in range(len(s)):
            c = s[r]
            if c in m:
                l = max(l, m[c])
            m[c] = r + 1
            maxSubStr = max(maxSubStr, r - l + 1)
        return maxSubStr

            
