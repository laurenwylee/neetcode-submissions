class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_dist = [math.inf] * len(points)
        min_dist[0] = 0
        seen = set()
        total = 0
        for _ in range(len(points)):
            min_u = math.inf
            min_i = None
            for i in range(len(points)):
                if tuple(points[i]) in seen:
                    continue
                if min_dist[i] < min_u:
                    min_u = min_dist[i]
                    min_i = i
            seen.add(tuple(points[min_i]))
            total += min_u
            for j, v in enumerate(points):
                if j == min_i:
                    continue
                if tuple(v) in seen:
                    continue
                dist = abs(points[min_i][0] - points[j][0]) + abs(points[min_i][1] - points[j][1])
                if dist < min_dist[j]:
                    min_dist[j] = dist
        return total
                

