class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # go from left to right and from right to left, first store leftProdcut, then multiply by rightProduct
        output = [0 for _ in range(len(nums))]
        leftProduct = 1
        for i in range(len(nums)):
            output[i] = leftProduct
            leftProduct *= nums[i]
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= rightProduct
            rightProduct *= nums[i]
        return output