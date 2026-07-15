class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ret = []
        for a, b in intervals:
            if a > end:
                ret.append([start, end])
                start = a
                end = b
            elif a <= start or b >= end:
                start = min(start, a)
                end = max(end, b)
        ret.append([start, end])
        return ret