class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for a, b in intervals[1:]:
            if a < prevEnd:
                print((a, b))
                count += 1
                prevEnd = min(b, prevEnd)
            else:
                prevEnd = b
        return count