class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        heap = [(grid[0][0], 0, 0)]
        distances = [[math.inf] * len(grid[0]) for _ in range(len(grid))]
        distances[0][0] = grid[0][0]
        while heap:
            dist, x, y = heapq.heappop(heap)
            for dx, dy in d:
                nx = dx + x
                ny = dy + y
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                if distances[nx][ny] <= max(grid[nx][ny], dist):
                    continue
                distances[nx][ny] = max(grid[nx][ny], dist)
                heapq.heappush(heap, (distances[nx][ny], nx, ny))
        return distances[len(grid) - 1][len(grid[0]) - 1]
        