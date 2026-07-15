class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x == y:
                continue
            if x < y:
                y = y - x
                heapq.heappush(heap, -y)
        if heap:
            return -heap[0]
        return 0