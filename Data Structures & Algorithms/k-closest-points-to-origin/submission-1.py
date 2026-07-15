class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x, y):
            return math.sqrt((x**2) + y**2)
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-getDistance(x, y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for d, x, y in heap:
            res.append([x, y])
        return res