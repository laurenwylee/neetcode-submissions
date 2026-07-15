class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        sq = defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in row[r]:
                        return False
                    else:
                        row[r].append(board[r][c])
                    if board[r][c] in col[c]:
                        return False
                    else:
                        col[c].append(board[r][c])
                    sq_idx = (r // 3) * 3 + (c // 3)
                    if board[r][c] in sq[sq_idx]:
                        return False
                    else:
                        sq[sq_idx].append(board[r][c])
        return True