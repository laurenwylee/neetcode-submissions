class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        start = []
        for x in nums:
            if x-1 not in d:
                start.append(x)
        m = 0
        for x in start:
            count = 0
            t = True
            i = x
            while t:
                if i in d:
                    count += 1
                    i += 1
                else:
                    t = False
            if count > m:
                m = count
        return m
            