class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0
        
        def getNeighbors(i, j):
            result = []
            if i > 0:
                result.append((i - 1, j))
            if i < len(grid) - 1: 
                result.append((i + 1, j))
            if j > 0:
                result.append((i, j - 1))
            if j < len(grid[0]) - 1:
                result.append((i, j + 1))
            return result

        def bfs(i, j):
            nonlocal numIslands
            queue = deque([(i, j)])
            while queue:
                ic, jc = queue.popleft()
                for ine, jne in getNeighbors(ic, jc):
                    if grid[ine][jne] == "1":
                        queue.append((ine, jne))
                        grid[ine][jne] = -1
            numIslands += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    bfs(i, j)

        return numIslands
                    
