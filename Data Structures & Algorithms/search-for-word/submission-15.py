class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        def dfs(i, j, idx):
            if idx >= len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] == word[idx]:
                original = board[i][j]
                board[i][j] = -1
                for dx, dy in d:
                    if dfs(i + dx, j + dy, idx + 1):
                        return True
                board[i][j] = original
            else:
                return False
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False