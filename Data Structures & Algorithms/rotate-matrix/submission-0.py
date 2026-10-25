class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # x x x x
        # x o h x 
        # x x x x
        # x x x x

        # first row becomes last column
        # second row becomes second last column
        # lets say we habe matrix[i][j] -> matrix[j][n - 1 - i]

        l, r = 0, len(matrix) - 1
        i = 0
        n = len(matrix)
        while i < len(matrix) and l < r:
            for j in range(l , r):
                el1, el2, el3, el4 = matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]
                matrix[j][n - 1 - i] = el1
                matrix[n - 1 - i][n - 1 - j] = el2
                matrix[n - 1 - j][i] = el3
                matrix[i][j] = el4
            i += 1
            l += 1
            r -= 1