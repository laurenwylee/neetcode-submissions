class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals:
            return intervals
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for _, (s, e) in enumerate(intervals, 1):
            if s <= end:
                end = max(e, end)
            else:
                result.append([start, end])
                start = s
                end = e
        result.append([start, end])
        return result
                