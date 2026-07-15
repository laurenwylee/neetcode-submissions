"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i: i.start)
        end = intervals[0].end
        for x in range(1, len(intervals)):
            if intervals[x].start < end:
                return False
            end = intervals[x].end
        return True
