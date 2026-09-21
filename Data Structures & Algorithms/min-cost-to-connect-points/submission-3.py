class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_dist = {}
        d = defaultdict(list)
        for i, (xi, yi) in enumerate(points):
            min_dist[(xi, yi)] = math.inf
            for j, (xj, yj) in enumerate(points[i+1:], start=i+1):
                distance = abs(xi - xj) + abs(yi - yj)
                d[(xi, yi)].append((distance, xj, yj))
                d[(xj, yj)].append((distance, xi, yi))
        
        heap = [(0, points[0][0], points[0][1])]
        seen = set()
        while heap:
            distance, xi, yi = heapq.heappop(heap)
            if (xi, yi) in seen:
                continue
            seen.add((xi, yi))
            min_dist[(xi, yi)] = distance
            for dist, xj, yj in d[(xi, yi)]:
                if (xj, yj) in seen:
                    continue
                heapq.heappush(heap, (dist, xj, yj))
        return sum(min_dist.values())

