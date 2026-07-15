class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x in points:
            dist = -1 * (math.sqrt(math.pow((x[0] - 0), 2) + math.pow((x[1] - 0), 2)))
            heapq.heappush(heap, [dist, x[0], x[1]])
        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        while heap:
            _,x,y = heapq.heappop(heap)
            result.append([x,y])
        return result
        