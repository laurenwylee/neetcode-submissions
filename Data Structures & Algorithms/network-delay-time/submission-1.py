class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        distances = [math.inf] * (n)
        distances[k - 1] = 0
        heap = [(0, k)]
        for ui, vi, ti in times:
            edges[ui].append((vi, ti))
        while heap:
            distance, node = heapq.heappop(heap)
            if distance <= distances[node - 1]:
                distances[node - 1] = distance
            else:
                continue
            for u, t in edges[node]:
                new_dist = distance + t
                if distances[u - 1] > new_dist:
                    distances[u- 1] = new_dist
                    heapq.heappush(heap, (new_dist, u))
        for x in distances:
            if x == math.inf:
                return -1
        return max(distances)