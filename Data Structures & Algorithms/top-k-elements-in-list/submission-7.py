class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency
        f = defaultdict(int)
        # count occurence
        o = defaultdict(list)

        for x in nums:
            f[x] += 1
            o[f[x]].append(x)
        
        for x in reversed(o.keys()):
            if len(o[x]) == k:
                return o[x]
            