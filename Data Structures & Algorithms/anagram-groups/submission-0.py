class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count each char
        # key is count of each char -> tuple
        # map tuple -> list

        m = defaultdict(list)
        char_m = {c: i for i, c in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[char_m[c]] += 1
            m[tuple(key)].append(s)
        res = list(m.values())
        return res
