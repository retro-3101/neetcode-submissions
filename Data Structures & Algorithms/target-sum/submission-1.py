class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i in range(1, n):
            for psum, count in dp[i-1].items():
                dp[i][psum+nums[i]] += count
                dp[i][psum-nums[i]] += count
        
        return dp[n-1][target]