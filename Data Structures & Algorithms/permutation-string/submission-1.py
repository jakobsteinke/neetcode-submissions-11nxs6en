class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(len(s1) * len(s2))
        counter1 = Counter(s1)
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1) - 1
        counter2 = defaultdict(int)
        for i in range(l, r):
            counter2[s2[i]] += 1
        while r < len(s2):
            counter2[s2[r]] += 1
            same = True
            for c in counter1.keys():
                if counter1[c] != counter2[c]:
                    same = False
            if same:
                return True
            counter2[s2[l]] -= 1
            l += 1
            r += 1
        return False