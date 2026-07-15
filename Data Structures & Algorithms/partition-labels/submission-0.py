class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(lambda: -1)
        for i in range(len(s)):
            d[s[i]] = max(d[s[i]], i)
        furthest = 0 
        ret = []
        start = 0
        for i in range(len(s)):
            furthest = max(d[s[i]], furthest)
            if i == furthest:
                ret.append(furthest - start + 1)
                start = furthest + 1
        return ret
