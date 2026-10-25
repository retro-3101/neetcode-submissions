class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)

        if not intervals:
            return [newInterval]

        flag = True

        result = []

        for i in range(n):

            if intervals[i][0] < newInterval[0]:
                result.append(intervals[i])
            
            elif flag:
                result.append(newInterval)
                result.append(intervals[i])
                flag = not flag
            
            else:
                result.append(intervals[i])
        
        if flag:
            result.append(newInterval)
        
        out = [result[0]]
        print(result, n)

        for i in range(1, n+1):

            if out[-1][1] >= result[i][0]:
                out[-1][1] = max(result[i][1], out[-1][1])
            
            else:
                out.append(result[i])
        
        return out