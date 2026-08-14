class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        intervals.sort()
        newStart = newInterval[0]
        newEnd = newInterval[1]
        for i, (start, end) in enumerate(intervals):
            if end < newStart:
                ret.append([start, end])
            elif start > newEnd:
                return ret + [[newStart, newEnd]] + intervals[i:]
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        ret.append([newStart, newEnd])
        return ret