class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dt = defaultdict(list)
        maxt = [float('inf') for _ in range(n+1)]
        maxt[k] = 0

        for time in times:
            dt[time[0]].append((time[2], time[1]))

        q = [(0, k)]

        while q:

            curr_time, node = heapq.heappop(q)

            if maxt[node] < curr_time:
                continue
            
            maxt[node] = curr_time

            for weight, neighbor in dt[node]:

                dist = weight + curr_time

                if dist < maxt[neighbor]:
                    heapq.heappush(q, (dist, neighbor))
        
        res = max(maxt[1:])

        if res == float('inf'):
            return -1

        return res 
