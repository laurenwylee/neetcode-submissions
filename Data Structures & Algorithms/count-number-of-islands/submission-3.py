class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return 
            if grid[x][y] != "1":
                return
            if grid[x][y] == "1":
                grid[x][y] = "0"
            for dx, dy in d:
                dfs(x + dx, y + dy)
        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    islands += 1
                    dfs(x, y)
        return islands