class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -1 * x)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if abs(x) != abs(y):
                y = abs(y) - abs(x)
                if y > 0:
                    y = y * -1
                heapq.heappush(heap, y)
        if heap == []:
            return 0
        else:
            return -1 * heap[0]
