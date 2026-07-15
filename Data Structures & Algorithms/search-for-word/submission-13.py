class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j, curr_char):
            if curr_char == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[curr_char]:
                return False
            if board[i][j] == None:
                return False
            if board[i][j] == word[curr_char]:
                board[i][j] = None
                for dx, dy in d:
                    if dfs(i + dx, j + dy, curr_char + 1):
                        return True
                board[i][j] = word[curr_char]
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False