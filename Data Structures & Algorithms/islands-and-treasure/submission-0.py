class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        inf = 2**31 - 1
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while queue:
            cur_i, cur_j, dist = queue.popleft()
            # logic
            

            for add_i, add_j in dirs:
                nei_i, nei_j = cur_i + add_i, cur_j + add_j
                if (
                    0 <= nei_i < len(grid) and 0 <= nei_j < len(grid[0]) 
                    and grid[nei_i][nei_j] == inf
                ):
                    queue.append((nei_i, nei_j, dist + 1))
                    grid[nei_i][nei_j] = dist + 1


