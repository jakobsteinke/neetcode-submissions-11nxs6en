class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1) - 1
        while r < len(s2):
            m = defaultdict(int)
            for i in range(l, r + 1):
                m[s2[i]] += 1
            same = True
            for c in counter.keys():
                if counter[c] != m[c]:
                    same = False
            if same:
                return True
            l += 1
            r += 1
        return False