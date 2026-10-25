class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for point in points:
            heapq.heappush(heap, (-math.sqrt(point[0]**2 + point[1]**2), (point[0], point[1])))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for point in heap:
            res.append(list(point[1]))

        return res