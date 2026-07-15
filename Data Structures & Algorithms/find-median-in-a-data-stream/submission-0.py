class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) > len(self.minHeap)+ 1:
            num = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2.0
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]