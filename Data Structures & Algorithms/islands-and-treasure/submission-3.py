class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2**31) - 1
        d = [[1, 0], [0, 1], [0,-1], [-1, 0]]
        queue = deque([])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    queue.append((x, y))
        layer = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                a, b = queue.popleft()
                for dx, dy in d:
                    nx = dx + a
                    ny = dy + b
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != INF:
                        continue
                    grid[nx][ny] = layer
                    queue.append((nx, ny))
            layer += 1
        # return grid

