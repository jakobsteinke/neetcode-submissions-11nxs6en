class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # (s1_idx, s2_idx)

        memo = {}

        def dfs(s1_idx, s2_idx):
            s3_idx = s1_idx + s2_idx
            if s1_idx == len(s1) and s2_idx == len(s2) and s3_idx == len(s3):
                return True
            if s3_idx >= len(s3):
                return False
            if (s1_idx, s2_idx) in memo:
                return memo[(s1_idx, s2_idx)]
            ans1 = ans2 = False
            if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
                ans1 = dfs(s1_idx + 1, s2_idx)
            if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                ans2 = dfs(s1_idx, s2_idx + 1)
            res = ans1 or ans2
            memo[(s1_idx, s2_idx)] = res
            return res

        return dfs(0, 0)

