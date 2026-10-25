class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[-float('inf'), float('inf')] for _ in range(n)]

        dp[0][0], dp[0][1] = nums[0], nums[0]

        maxp = dp[0][0]

        for i in range(1, n):
            a, b, c = dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i]

            dp[i][0] = max(a, b, c)
            dp[i][1] = min(a, b, c)
            maxp = max(maxp, dp[i][0])

        return maxp  