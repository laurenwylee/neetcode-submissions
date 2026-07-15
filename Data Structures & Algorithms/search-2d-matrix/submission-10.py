class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])
        l = 0
        r = (rows * col) - 1
        while l <= r:
            mid = l + (r - l) // 2
            ro = mid // col
            c = mid % col
            if matrix[ro][c] < target:
                l = mid + 1
            elif matrix[ro][c] > target:
                r = mid - 1
            else:
                return True
        return False
