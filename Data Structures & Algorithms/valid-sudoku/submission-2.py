class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # i = 0, while i < len(board)
            # j = 0, while j < len(board[i])
                # for a in range(i, i + 3):
                    # for b in range(j, j + 3)
            #.j += 3
        #. i += 3

        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                s = set()
                for y in range(i, i + 3):
                    for x in range(j, j + 3):
                        if board[y][x] in s:
                            return False
                        if board[y][x] != ".":
                            s.add(board[y][x])
                j += 3
            i += 3

        for i in range(len(board)):
            s = set()
            for j in range(len(board[i])):
                if board[i][j] in s:
                    return False
                if board[i][j] != ".":
                    s.add(board[i][j])

        for j in range(len(board[0])):
            s = set()
            for i in range(len(board[j])):
                if board[i][j] in s:
                    return False
                if board[i][j] != ".":
                    s.add(board[i][j])

        return True
