class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def column_search(r, lc, rc, matrix, target):
            if lc > rc:
                return False
            pivot = (lc + rc) // 2
            if matrix[r][pivot] == target:
                return True
            elif matrix[r][pivot] < target:
                return column_search(r, pivot + 1, rc, matrix, target)
            else:
                return column_search(r, lc, pivot - 1, matrix, target)

        def row_search(lr, rr, matrix, target):
            if lr > rr:
                return False
            pivot = (lr + rr) // 2
            if matrix[pivot][0] == target:
                return True
            elif matrix[pivot][0] < target:
                if matrix[pivot][len(matrix[pivot])-1] >= target:
                    return column_search(pivot, 0, len(matrix[pivot])-1, matrix, target)
                # column_search(pivot, 0, len(matrix[pivot])-1, matrix, target):
                #     return True
                else:
                    return row_search(pivot + 1, rr, matrix, target)
            else:
                return row_search(lr, pivot - 1, matrix, target)
        return row_search(0, len(matrix)-1, matrix, target)