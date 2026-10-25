"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        time = []

        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))

        res, count = 0, 0

        for _, state in time:
            count += state
            res = max(count, res)

        return res