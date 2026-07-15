class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        l = 0
        r = (cols * rows) - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        # rows = len(matrix)
        # col = len(matrix[0])
        # l = 0
        # r = (rows * col) - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     ro = mid // col
        #     c = mid % col
        #     if matrix[ro][c] < target:
        #         l = mid + 1
        #     elif matrix[ro][c] > target:
        #         r = mid - 1
        #     else:
        #         return True
        # return False
