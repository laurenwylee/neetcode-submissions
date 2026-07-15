class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            total = 1
            for dx, dy in d:
                total += dfs(x + dx, y + dy)
            return total
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    res = max(res, dfs(x, y))
        return res