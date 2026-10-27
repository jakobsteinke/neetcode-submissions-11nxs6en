class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq for char
        char_count1 = [0] * 26
        window_count2 = [0] * 26
        for c in s1:
            char_count1[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            window_count2[ord(s2[r]) - ord('a')] += 1
            while window_count2[ord(s2[r]) - ord('a')] > char_count1[ord(s2[r]) - ord('a')] :
                window_count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if char_count1 == window_count2:
                return True
        
        return False
            

