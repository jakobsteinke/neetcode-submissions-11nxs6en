class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        maxTime = 0

        while queue:
            ci, cj, ct = queue.popleft()
            maxTime = max(maxTime, ct)
            for ni, nj in getNeis(ci, cj):
                if grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, ct + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return maxTime