class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        def helper(nums):
            n = len(nums)

            if n == 1:
                return nums[0]

            dp = [0 for i in range(n)]

            dp[0], dp[1] = nums[0], max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[n-1]
        
        return max(helper(nums1), helper(nums2))