class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        intervals.sort()
        newStart = newInterval[0]
        newEnd = newInterval[1]
        for start, end in intervals:
            if end < newStart:
                ret.append([start, end])
            elif start > newEnd:
                ret.append([start, end])
            elif newStart >= start or newEnd <= end:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        for i, (start, end) in enumerate(ret):
            if start > newEnd:
                ret.insert(i, [newStart, newEnd])
                return ret
        ret.append([newStart, newEnd])
        return ret