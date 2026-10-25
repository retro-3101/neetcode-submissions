class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. build a max-heap of remaining counts
        ready = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(ready)

        cooldown = deque()          # (ready_at_time, -remaining_count)
        time = 0

        while ready or cooldown:
            time += 1                                   # 1 tick

            # step-1: if something is ready, run it
            if ready:
                cnt = heapq.heappop(ready) + 1          # one copy executed
                if cnt:                                 # more copies left
                    cooldown.append((time + n, cnt))    # add to cooldown

            # step-2: move tasks whose cooldown expired back to heap
            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(ready, cnt)

        return time