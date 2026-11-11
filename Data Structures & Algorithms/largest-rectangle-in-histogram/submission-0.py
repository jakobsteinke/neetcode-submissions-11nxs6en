class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start_idx = i
            counter = 1
            while stack and stack[-1][0] > height:
                cur, j = stack.pop()
                max_area = max(max_area, cur * (i - j))
                counter += 1
                start_idx = j
            stack.append((height, start_idx))
            max_area = max(max_area, height * (i - start_idx + 1))

        i = len(heights) - 1
        while stack:
            cur, j = stack.pop()
            max_area = max(max_area, cur * (i - j + 1))

        return max_area
