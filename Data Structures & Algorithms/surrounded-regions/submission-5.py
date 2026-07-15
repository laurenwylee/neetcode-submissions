class Solution:
    def solve(self, board: List[List[str]]) -> None:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return 
            if board[x][y] == "X" or board[x][y] == "Z":
                return
            board[x][y] = "Z"
            for dx, dy in d:
                dfs(x + dx, y + dy)
        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                dfs(i, len(board[0]) - 1)
        for i in range(1, len(board[0])):
            if board[0][i] == "O":
                dfs(0, i)
            if board[len(board) - 1][i] == "O":
                dfs(len(board) - 1, i)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "Z":
                    board[x][y] = "O"