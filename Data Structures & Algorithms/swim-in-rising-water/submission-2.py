class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        distances = [[math.inf] * len(grid[0]) for _ in range(len(grid))]
        di = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while heap:
            d, x, y = heapq.heappop(heap)
            if d <= distances[x][y]:
                distances[x][y] = d
            else:
                continue
            for dx, dy in di:
                nx = dx + x
                ny = dy + y
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                new_dist = max(d, grid[nx][ny])
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(heap, (new_dist, nx, ny))
        return distances[len(grid) - 1][len(grid[0]) - 1]
                    