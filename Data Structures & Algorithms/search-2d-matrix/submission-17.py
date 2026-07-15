class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            mid = l + (r - l) // 2
            m_val = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if m_val == target:
                return True
            if m_val < target:
                l = l + 1
            else:
                r = r - 1
            
        return False