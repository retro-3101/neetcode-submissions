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
        
        return -heapq.heappop(neg_stones) if neg_stones else 0