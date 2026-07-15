class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        b = [[0] * len(board[0]) for _ in range(len(board))]
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(x, y, i):
            if i == len(word) - 1:
                return True
            for j in d:
                if x + j[0] >= 0 and x + j[0] < len(board) and y + j[1] >= 0 and y + j[1] < len(board[0]) and b[x + j[0]][y + j[1]] == 0 and board[x + j[0]][y + j[1]] == word[i + 1]:
                    b[x + j[0]][y + j[1]] += 1
                    if dfs(x + j[0], y + j[1], i + 1):
                        return True
                    b[x + j[0]][y + j[1]] -= 1
            return False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    b[x][y] += 1
                    if dfs(x, y, 0):
                        return True
                    b[x][y] -= 1
        return False


























        # b = [[0] * len(board[0]) for _ in range(len(board))]
        # d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # def dfs(x, y, i):
        #     print(board[x][y])
        #     if i == len(word) - 1:
        #         return True
        #     for j in d:
        #         if x + j[0] < 0 or x + j[0] >= len(board) or y + j[1] < 0 or y + j[1] >= len(board[0]) or b[x + j[0]][y + j[1]] > 0 or board[x+j[0]][y+j[1]] != word[i+1]:
        #             continue
        #         b[x + j[0]][y + j[1]] += 1
        #         if dfs(x + j[0], y + j[1], i + 1):
        #             return True
        #         b[x + j[0]][y + j[1]] -= 1
        #     return False

        # for x in range(len(board)):
        #     for y in range(len(board[0])):
        #         b[x][y] += 1
        #         if board[x][y] == word[0] and dfs(x, y, 0):
        #             return True
        #         b[x][y] -= 1
        # return False