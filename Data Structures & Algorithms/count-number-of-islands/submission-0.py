class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if grid[x][y] == "1":
                grid[x][y] = "0"
                if x - 1 >= 0 :
                    dfs(x - 1, y)
                if x + 1 < len(grid):
                    dfs(x + 1, y)
                if y - 1 >= 0:
                    dfs(x, y - 1)
                if y + 1 < len(grid[x]):
                    dfs(x, y  + 1)
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    dfs(x, y)
                    count += 1
        return count
