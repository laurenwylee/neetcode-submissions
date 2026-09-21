class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = [(0, 0, 0)]
        distances = [[math.inf] * len(heights[0]) for _ in range(len(heights))]
        distances[0][0] = 0
        while heap:
            dist, x, y = heapq.heappop(heap)
            if dist > distances[x][y]: 
                continue
            for dx, dy in d:
                nx = dx + x
                ny = dy + y
                if nx < 0 or nx >= len(heights) or ny < 0 or ny >= len(heights[0]):
                    continue
                nd = max(dist, abs(heights[nx][ny] - heights[x][y]))
                if distances[nx][ny] <= nd:
                    continue
                distances[nx][ny] = nd
                heapq.heappush(heap, (nd, nx, ny))
        return distances[len(heights) - 1][len(heights[0]) - 1]
                