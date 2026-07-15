class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]  * n for x in range(n)]
        count = [[0] * n for x in range(n)]
        result = []
        def dfs(x, y, i):
            if i == n - 1:
                curr = []
                for i in range(n):
                        s = "".join(board[i])
                        curr.append(s)
                result.append(curr)
                return True
            for j in range(n):
                if count[x + 1][j] == 0:
                    updateCount(x+1, j, 1)
                    board[x+1][j] = "Q"
                    dfs(x+1, j, i+1)
                    updateCount(x+1, j, -1)
                    board[x+1][j] = "."
            return False
            
        
        def updateCount(x, y, i):
            for j in range(n):
                for k in range(n):
                    if j == x or k == y:
                        count[j][k] += i
            j = x + 1
            k = y + 1
            while j < n and k < n:
                count[j][k] += i
                j += 1
                k += 1
            j = x - 1
            k = y - 1
            while j >= 0 and k >= 0:
                count[j][k] += i
                j -= 1
                k -= 1
            j = x + 1
            k = y - 1
            while j < n and k >= 0:
                count[j][k] += i
                j += 1
                k -= 1
            j = x - 1
            k = y + 1
            while j >= 0 and k < n:
                count[j][k] += i
                j -= 1
                k += 1

        for y in range(n):
            updateCount(0, y, 1)
            board[0][y] = "Q"
            dfs(0, y, 0)
            updateCount(0, y, -1)
            board[0][y] = "."
        return result
        