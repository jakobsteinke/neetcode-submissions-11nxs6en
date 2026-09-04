class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def getNeis(i, j):
            result = []
            if i > 0:
                result.append((i - 1, j))
            if i + 1 < len(grid):
                result.append((i + 1, j))
            if j > 0:
                result.append((i, j - 1))
            if j + 1 < len(grid[i]):
                result.append((i, j + 1))
            return result

        def bfs(i, j):
            nonlocal maxArea
            queue = deque([(i, j)])
            area = 0
            while queue:
                ci, cj = queue.popleft()
                area += 1
                for neI, neJ in getNeis(ci, cj):
                    if grid[neI][neJ] == 1:
                        grid[neI][neJ] = -1 
                        queue.append((neI, neJ))                   
            maxArea = max(maxArea, area)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = -1 
                    bfs(i, j)

        return maxArea