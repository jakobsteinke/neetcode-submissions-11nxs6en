class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()

        def bfs(i, j):
            queue = deque([(i, j)])
            mark = False
            markList = []
            while queue:
                ci, cj = queue.popleft()
                markList.append((ci, cj))
                for ai, aj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (
                        ci + ai < 0 or ci + ai == len(board) or
                        cj + aj < 0 or cj + aj == len(board[0])
                        or board[ci + ai][cj + aj] != 'O' or
                        (ci + ai, cj + aj) in seen
                    ):
                        continue
                    if (
                        ci + ai == 0 or ci + ai == len(board) - 1 or
                        cj + aj == 0 or cj + aj == len(board[0]) - 1
                    ):
                        mark = True
                    seen.add((ci + ai, cj + aj))
                    queue.append((ci + ai, cj + aj))
            if not mark:
                for mi, mj in markList:
                    board[mi][mj] = 'X'


        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if board[i][j] == 'O' and (i, j) not in seen:
                    seen.add((i, j))
                    bfs(i, j)