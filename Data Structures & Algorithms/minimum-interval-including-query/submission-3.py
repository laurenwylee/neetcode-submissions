class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1] * len(queries)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        intervals.sort()

        curr_i = 0
        heap = []
        for q, i in sorted_queries:
            while curr_i < len(intervals) and intervals[curr_i][0] <= q:
                heapq.heappush(heap, (intervals[curr_i][1] - intervals[curr_i][0] + 1, intervals[curr_i]))
                curr_i += 1
            while heap:
                # print(heap)
                space, [start, end] = heap[0]
                if end < q:
                    heapq.heappop(heap)
                    continue
                result[i] = space
                break
        return result
                

