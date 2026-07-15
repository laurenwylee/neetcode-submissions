class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_count = 0
        self.curr_count = 0
        def dfs(x, y):
            if grid[x][y] == 1:
                self.curr_count += 1
                grid[x][y] = 0
                if x - 1 >= 0:
                    dfs(x-1, y)
                if y - 1 >= 0:
                    dfs(x, y-1)
                if x + 1 < len(grid):
                    dfs(x+ 1, y)
                if y + 1 < len(grid[0]):
                    dfs(x, y+1)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    self.curr_count = 0
                    dfs(x, y)
                    self.max_count = max(self.max_count, self.curr_count)
        return self.max_count





























        # def dfs(x, y):
        #     if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
        #         return 0
        #     else:
        #         if grid[x][y] == 1:
        #             grid[x][y] = 0
        #             return 1 + (dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x, y - 1))
        #         else:
        #             return 0
            
        # m = 0
        # for x in range(len(grid)):
        #     for y in range(len(grid[x])):
        #         if grid[x][y] == 1:
        #             m = max(m, dfs(x, y))

        # return m
