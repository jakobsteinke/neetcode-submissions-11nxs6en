class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific traversal
        data = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]

        def bfs(ocean, queue):  
            while queue:
                r, c = queue.popleft()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr >= 0 and nr < len(heights) and nc >= 0 and nc < len(heights[0]) 
                        and not data[nr][nc][ocean] and heights[nr][nc] >= heights[r][c]
                    ):
                        data[nr][nc][ocean] = True
                        queue.append((nr, nc))
        queue = deque()
        for i in range(len(heights[0])):
            queue.append((0, i))
            data[0][i][0] = True 

        for i in range(1, len(heights)):
            queue.append((i, 0))
            data[i][0][0] = True 
        bfs(0, queue)

        queue = deque()
        for i in range(len(heights[0])):
            queue.append((len(heights) - 1, i))
            data[len(heights) - 1][i][1] = True 

        for i in range(len(heights) - 1):
            queue.append((i, len(heights[0]) - 1))
            data[i][len(heights[0]) - 1][1] = True 
        bfs(1, queue)

        count = 0
        result = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j][0] and data[i][j][1]:
                    result.append([i, j])

        return result


        
                    




