class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, dest, price in flights:
            graph[source].append((price, dest))
        distances = [[math.inf] * n for _ in range(k + 2)]
        visited = set()
        heap = [(0, src, 0)]
        distances[0][src] = 0
        while heap:
            dist, nd, flights = heapq.heappop(heap)
            if flights == k+ 1:
                continue
            if dist > distances[flights][nd]:
                continue
            for d, u in graph[nd]:
                new_dest = dist + d 
                if new_dest < distances[flights + 1][u]:
                    distances[flights + 1][u] = new_dest
                    heapq.heappush(heap, (new_dest, u, flights + 1))
        min_cost = math.inf
        for i in range(k + 2):
            min_cost = min(distances[i][dst], min_cost)
        if min_cost != math.inf:
            return min_cost
        return -1

                    