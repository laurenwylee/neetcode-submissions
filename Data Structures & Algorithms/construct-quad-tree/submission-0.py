"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if grid[0][0] == 0:
            zero_grid = True
        else:
            zero_grid = False
        isLeaf = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and zero_grid:
                    isLeaf = False
                    break
                if grid[i][j] == 0 and not zero_grid:
                    isLeaf = False
                    break
        if isLeaf:
            return Node(not zero_grid, True)
        else:
            mid = len(grid) // 2
            topLeft = [row[:mid] for row in grid[:mid]]
            topRight = [row[mid:] for row in grid[:mid]]
            bottomLeft = [row[:mid] for row in grid[mid:]]
            bottomRight = [row[mid:] for row in grid[mid:]]
            return Node(zero_grid, False, self.construct(topLeft), self.construct(topRight), self.construct(bottomLeft), self.construct(bottomRight))
