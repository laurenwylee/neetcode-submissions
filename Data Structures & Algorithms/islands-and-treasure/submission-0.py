class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        d = [[0, 1], [1, 0], [0,-1], [-1, 0]]
        q = deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    q.append([x, y])
        while q:
            currx, curry = q.popleft()
            for dx, dy in d:
                if currx + dx >= 0 and currx + dx < len(grid) and curry + dy >= 0 and curry + dy < len(grid[0]) and grid[currx + dx][curry + dy] == 2147483647:
                    grid[currx+dx][curry+dy] = grid[currx][curry] + 1
                    q.append([currx+dx, curry+dy])
        


















        # d = [[0, 1], [1, 0], [0,-1], [-1, 0]]
        # def traverse(x, y, i):
        #     for dx, dy in d:
        #         if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or y + dy >= len(grid) or grid[x+dx][y+dy] == -1:
        #             continue
        #         if grid[x+dx][y+dy] == 0:
        #             grid[x+dx][y+dy] = i
            
        # for x in range(len(grid)):
        #     for y in range(len(grid[0])):
        #         if grid[x][y] ==  2147483647:
        #             traverse(x, y)
