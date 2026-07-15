class Solution:
    def solve(self, board: List[List[str]]) -> None:
        d = [[0,1], [0,-1], [1,0],[-1,0]]
        def dfs(x, y):
            if x >= len(board) or x < 0 or y < 0 or y >= len(board[0]):
                return
            if board[x][y] != "O":
                return
            board[x][y] = "S"
            for dx, dy in d:
                dfs(dx+x, dy+y)

        for x in range(len(board)):
            if board[x][0] == "O":
                dfs(x, 0)
            if board[x][len(board[0])-1] == "O":
                dfs(x, len(board[0])-1)
        for y in range(1, len(board[0])-1):
            if board[0][y] == "O":
                dfs(0, y)
            if board[len(board)-1][y] == "O":
                dfs(len(board)-1, y)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "S":
                    board[x][y] = "O"