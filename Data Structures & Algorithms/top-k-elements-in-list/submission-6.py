class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for x in nums:
            if x not in m.keys():
                m[x] = 1
            else:
                m[x] += 1
        bucket = [None] * len(nums)
        for i in m.keys():
            if bucket[m[i] - 1] == None:
                bucket[m[i] - 1] = [i]
            else:
                bucket[m[i] - 1].append(i)
        res = []
        for x in range(len(bucket)-1, -1, -1):
            if bucket[x] != None:
                k = k - len(bucket[x])
                res = res + bucket[x]
                if k <= 0:
                    return res
