class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # map elem -> index of last occurrence 
        longestSubstring = 0
        currentSubstringLen = 0
        lastDUplicatePosition = 0
        m = {}
        for i in range(len(s)):
            c = s[i]
            if c in m: 
                lastDUplicatePosition = max(m[c], lastDUplicatePosition)
                currentSubstringLen = i - lastDUplicatePosition
            else:
                currentSubstringLen += 1
            m[c] = i
            longestSubstring = max(longestSubstring, currentSubstringLen)
        
        return longestSubstring
            
