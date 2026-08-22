class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, remainingWord):
            if not remainingWord:
                return True
            if (
                i >= len(board) or i < 0 or j >= len(board[i]) or j < 0 or
                board[i][j] != remainingWord[0]
            ):
                return False
            c = board[i][j]
            board[i][j] = -1
            if (
                dfs(i + 1, j, remainingWord[1:]) or dfs(i - 1, j, remainingWord[1:]) or
                dfs(i, j + 1, remainingWord[1:]) or dfs(i, j - 1, remainingWord[1:])
            ):
                return True
            board[i][j] = c
            return False
        
        found = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                found = found or dfs(i, j, word)
        return found