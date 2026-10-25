class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        self.h = h
        best_k = r

        while r>l:

            mid =  (l+r)//2

            if self.helper(piles, mid):
                r = mid
            
            else:
                l = mid+1
            
            best_k = min(r, best_k)
        
        return best_k

    def helper(self, piles: List[int], k: int) -> bool:
        
        count = 0
        for i in range(len(piles)):

            count += math.ceil(piles[i]/k)
        
        return self.h >= count
        