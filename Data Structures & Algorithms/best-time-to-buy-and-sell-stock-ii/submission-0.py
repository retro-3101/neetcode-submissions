class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profits, prev = 0, prices[0]

        for num in prices[1:]:
            profits += (num-prev) if (num-prev) > 0 else 0

            prev = num
        
        return profits