class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        countzero = 0
        prod = 1

        for num in nums:
            if num == 0:
                countzero += 1
            else:
                prod *= num
        
        res = [0] * len(nums)
        if countzero > 1:
            return res
        
        elif countzero == 1:

            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
            
            return res
        
        else:

            for i in range(len(nums)):
                res[i] = int(prod / nums[i])
            
        return res
