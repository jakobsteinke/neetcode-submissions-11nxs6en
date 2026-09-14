class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                result.append(cur)
                return
            if cur_sum > target or i == len(candidates):
                return
            # either appned curent element
            cur.append(candidates[i])
            cur_sum += candidates[i]
            dfs(i + 1, cur.copy(), cur_sum)
            # or skip to next disticnt num
            cur.pop()
            cur_sum -= candidates[i]
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            dfs(i, cur.copy(), cur_sum)

        dfs(0, [], 0)
        return result

            