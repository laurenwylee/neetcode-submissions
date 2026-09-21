class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for a, b, time in times:
            edges[a].append((b, time))

        distances = [math.inf] * n
        distances[k - 1] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time > distances[node - 1]:
                continue
            for u, t in edges[node]:
                if t + time < distances[u - 1]:
                    distances[u - 1] = t + time
                    heapq.heappush(heap, (t + time, u))
        if max(distances) == math.inf:
            return -1
        return max(distances)