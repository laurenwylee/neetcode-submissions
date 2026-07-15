class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        def isValid(x, y, sub):
            if x < 0 or y < 0 or x >= n or y >= n:
                return False 
            rightDiag = y - 1
            leftDiag = y + 1
            for i in range(x-1, -1, -1):
                if sub[i][y] == "Q":
                    return False
                if rightDiag >= 0 and rightDiag < n:
                    if sub[i][rightDiag] == "Q":
                        return False
                if leftDiag >= 0 and leftDiag < n:
                    if sub[i][leftDiag] == "Q":
                        return False
                rightDiag -= 1
                leftDiag += 1
            return True
                
        def dfs(x, y, sub):
            if x == n:
                ret.append(sub.copy())
                return
            if y == n:
                return
            if isValid(x, y, sub):
                # change sub
                sub[x] = sub[x][:y] + "Q" + sub[x][y + 1:]
                dfs(x + 1, 0, sub)
                sub[x] = sub[x][:y] + "." + sub[x][y + 1:]
            # change back sub
            dfs(x, y + 1, sub)
        sub = ["." * n for _ in range(n)]
        dfs(0, 0, sub )
        return ret