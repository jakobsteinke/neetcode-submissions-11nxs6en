class Solution:
    def trap(self, height: List[int]) -> int:
        # move r until its height is gretaer or equal height of l 
        # until then count number of blocks
        # if r reaches end, traverse backward from r to last l and do same thing 

        l, r = 0, 1
        block_count = 0
        water_count = 0
        while r < len(height):
            if height[r] >= height[l]:
                water_count += (r - l - 1) * height[l] - block_count
                block_count = 0
                l = r
            else:
                block_count += height[r]
            r += 1
        if l != r - 1:
            block_count = 0
            end = l
            l = r - 1
            r = r - 2
            while r >= end:
                if height[r] >= height[l]:
                    water_count += (l - r - 1) * height[l] - block_count
                    block_count = 0
                    l = r
                else:
                    block_count += height[r]
                r -= 1
        return water_count


            
            
