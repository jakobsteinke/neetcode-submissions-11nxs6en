class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def getNeis(i, j):
            result = []
            if i > 0:
                result.append((i - 1, j))
            if i + 1 < len(heights):
                result.append((i + 1, j))
            if j > 0:
                result.append((i, j - 1))
            if j + 1 < len(heights[i]):
                result.append((i, j + 1))
            return result

        queue = deque()
        mark = [
            [[False, False] for _ in range(len(heights[0]))]
            for _ in range(len(heights))
        ]        
        # enqueue P
        for i in range(len(heights[0])):
            mark[0][i][0] = True
            queue.append((0, i))
        for i in range(len(heights)):
            mark[i][0][0] = True
            queue.append((i, 0))
        # enqueue A
        for i in range(len(heights[0])):
            mark[len(heights) - 1][i][1] = True
            queue.append((len(heights) - 1, i))
        for i in range(len(heights)):
            mark[i][len(heights[0]) - 1][1] = True
            queue.append((i, len(heights[0]) - 1))

        while queue:
            ci, cj = queue.popleft()
            ChasP, ChasA = mark[ci][cj]
            for ni, nj in getNeis(ci, cj):
                NhasP, NhasA = mark[ni][nj]
                if NhasP == ChasP and NhasA == ChasA or heights[ni][nj] < heights[ci][cj]:
                    continue
                mark[ni][nj] = [NhasP or ChasP, NhasA or ChasA]
                queue.append((ni, nj))

        result = []
        for i in range(len(mark)):
            for j in range(len(mark[i])):
                if mark[i][j] == [True, True]:
                    result.append([i, j])

        return result

            