class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        curr = intervals[0][1]
        res = 0

        for i in range(1, n):

            if curr > intervals[i][0]:
                res += 1
                curr = min(intervals[i][1], curr)
            
            else:
                curr = intervals[i][1]

        return res 