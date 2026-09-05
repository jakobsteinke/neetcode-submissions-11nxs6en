class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLength = 1
        for i in range(len(s)):
            # try odd palindrome from here
            l, r = i - 1, i + 1
            counter = 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    counter += 2
                else:
                    break
                l -= 1
                r += 1
            if counter > resLength:
                res = l + 1
                resLength = counter
            # try evel palindrome from here
            l, r = i, i + 1
            counter = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    counter += 2
                else:
                    break
                l -= 1
                r += 1
            if counter > resLength:
                res = l + 1
                resLength = counter
        return s[res:res + resLength]