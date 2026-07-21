class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            midx = mid % len(matrix[0])
            midy = mid // len(matrix[0])

            if matrix[midy][midx] == target:
                return True
            elif matrix[midy][midx] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False