class Solution:
    def countSubstrings(self, s: str) -> int:
        palCounter = len(s)
        for i in range(len(s)):
            # try odd palindrome from here
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    palCounter += 1
                else:
                    break
                l -= 1
                r += 1
            # try evel palindrome from here
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    palCounter += 1
                else:
                    break
                l -= 1
                r += 1
        return palCounter