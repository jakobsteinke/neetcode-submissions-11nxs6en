class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # one pass from start to end
        # one pass from end to start
        # keep track of max product
        maxProduct = -math.inf
        curProduct = 1
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                curProduct *= num
                maxProduct = max(maxProduct, curProduct)
            else:
                curProduct = 1
                maxProduct = max(maxProduct, 0)
        curProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num != 0:
                curProduct *= num
                maxProduct = max(maxProduct, curProduct)
            else:
                curProduct = 1
                maxProduct = max(maxProduct, 0)
        return maxProduct
        
