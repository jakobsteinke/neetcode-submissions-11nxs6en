class Solution:

    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        
        def checkIfValid(counter):
            for c in t_counter.keys():
                if counter[c] < t_counter[c]:
                    return False
            return True

        l = 0
        bl, br = -1, -1
        s_counter = defaultdict(int)

        for r in range(len(s)):
            s_counter[s[r]] += 1
            while checkIfValid(s_counter):
                if r - l + 1 < br - bl + 1 or br == -1:
                    bl = l
                    br = r
                s_counter[s[l]] -= 1
                l += 1
        
        res = []
        for i in range(bl, br + 1):
            res.append(s[i])

        return "".join(res) if bl != -1 else ""

