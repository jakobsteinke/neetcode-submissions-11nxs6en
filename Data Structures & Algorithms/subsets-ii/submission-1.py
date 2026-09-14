class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # append result and do i + 1 or append cur to result and shif i to next non duplicate 
        # sort
        # skip duplicates


        #  2222
        #  you don't want to have these: 0222, 0022, 0202, 0220, 0002, 0020, 0200
        # so either append current num to current or skip to next non duplicate num
        # that way you get: 2222, 2220, 2200, 2000, 0000
        # (0 stands for not append to result)
        
        nums.sort()
        result = []
        def dfs(i, cur):
            if i == len(nums):
                result.append(cur)
                return
            cur.append(nums[i])
            dfs(i + 1, cur.copy())
            cur.pop()
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i, cur)
        
        dfs(0, [])
        return result 
