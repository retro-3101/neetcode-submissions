class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #kadane's algo
        res = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            total = nums[i] if total<0 else total+nums[i]
            res = max(total, res)
        
        return res

            