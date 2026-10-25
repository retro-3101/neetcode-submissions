class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        halfsum = sum(nums)//2

        if halfsum != sum(nums)/2:
            return False

        dp = [False]*(halfsum+1)
        dp[0] = True

        for num in nums:
            for i in range(halfsum, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[halfsum]
        
            
