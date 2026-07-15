class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        heap = []
        for n in nums:
            d[n] += 1
            heapq.heappush(heap, (n, d[n]))
            while len(heap) > k:
                heapq.heappop(heap)
        return heap[0][0]