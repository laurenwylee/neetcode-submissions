class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([])
        num_fresh = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append((x, y))
                if grid[x][y] == 1:
                    num_fresh += 1
        if num_fresh == 0:
            return 0
        layer = -1
        while queue:
            length = len(queue)
            for _ in range(length):
                x, y = queue.popleft()
                for dx, dy in d:
                    nx = dx + x
                    ny = dy + y
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                        continue
                    if grid[nx][ny] == 1:
                        num_fresh -= 1
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
            layer += 1
            
        if num_fresh != 0:
            return -1
        return layer
