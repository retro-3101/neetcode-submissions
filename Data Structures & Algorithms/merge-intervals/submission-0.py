class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        out = [intervals[0]]

        for i in range(1, n):

            if out[-1][1] >= intervals[i][0]:
                out[-1][1] = max(intervals[i][1], out[-1][1])
            
            else:
                out.append(intervals[i])
        
        return out