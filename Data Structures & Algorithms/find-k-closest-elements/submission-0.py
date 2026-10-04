class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            dist = abs(x - arr[i])
            heapq.heappush(heap, (dist, arr[i]))
        res = []
        for i in range(min(k, len(heap))):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)