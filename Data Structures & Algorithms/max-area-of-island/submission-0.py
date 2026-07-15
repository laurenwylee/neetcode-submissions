class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
                return 0
            else:
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    return 1 + (dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x, y - 1))
                else:
                    return 0
            
        m = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    m = max(m, dfs(x, y))

        return m
