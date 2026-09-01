class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = {}
        # rows:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if num < 1 or num > 9 or num in m:
                        return False
                    m[num] = True
            m.clear()

        # columns:
        for j in range(9):
            for i in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if num < 1 or num > 9 or num in m:
                        return False
                    m[num] = True
            m.clear()

        # grid boxes
        for y in range(3):
            for x in range(3):
                for i in range(3 * y, 3 * y + 3):
                    for j in range(3 * x, 3 * x + 3):
                        if board[i][j] != '.':
                            num = int(board[i][j])
                            if num < 1 or num > 9 or num in m:
                                return False
                            m[num] = True
                m.clear()    

        return True