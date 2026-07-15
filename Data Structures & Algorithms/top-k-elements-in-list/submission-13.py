class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for n in d:
            freq[d[n]].append(n)
        ret = []
        for i in range(len(freq) - 1, -1, -1):
            for x in freq[i]:
                ret.append(x)
                if len(ret) == k:
                    return ret



        # d = defaultdict(int)
        # for n in nums:
        #     d[n] += 1
        # heap = []
        # for n in d:
        #     if len(heap) < k:
        #         heapq.heappush(heap, (d[n], n))
        #         continue
        #     if heap[0][0] < d[n]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, (d[n], n))
        # return [x[1] for x in heap]
