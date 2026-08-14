class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        ret = []
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s <= end:
                start = min(start, s)
                end = max(end, e)
            else:
                ret.append([start, end])
                start = s
                end = e
        ret.append([start, end])
        return ret
