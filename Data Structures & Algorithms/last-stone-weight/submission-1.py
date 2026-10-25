class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        neg_stones = [-stone for stone in stones]

        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:

            a = -heapq.heappop(neg_stones)
            b = -heapq.heappop(neg_stones)

            if a==b:
                continue
            else:
                heapq.heappush(neg_stones, -abs(a-b))
        
        if len(neg_stones):
            return -heapq.heappop(neg_stones)
        
        return 0