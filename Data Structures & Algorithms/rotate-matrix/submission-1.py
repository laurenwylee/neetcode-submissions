class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # if cant go left, go down
        # if cant go down, go right
        # if cant go right, go up
        for i in range((len(matrix)) // 2):
            for j in range(len(matrix[0])):
                matrix[i][j], matrix[len(matrix) - i - 1][j] = matrix[len(matrix) - i - 1][j], matrix[i][j]
        for c in range(len(matrix)):
            for r in range(c + 1, len(matrix)):
                matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]