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
                if grid[ci][cj] == 1:
                    area += 1
                    grid[ci][cj] = -1
                    for nei in getNeis(ci, cj):
                        queue.append(nei)                    
            maxArea = max(maxArea, area)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    bfs(i, j)

        return maxArea