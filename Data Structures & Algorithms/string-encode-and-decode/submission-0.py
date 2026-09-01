class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            word = ''
            for _ in range(length):
                word += s[i]
                i += 1
            result.append(word)
        return result
