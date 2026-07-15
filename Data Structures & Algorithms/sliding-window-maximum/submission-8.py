class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        result = []
        result.append(-heap[0][0])
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r],r))
            while heap and heap[0][1] <= (r - k):
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result