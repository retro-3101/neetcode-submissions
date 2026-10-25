class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table = {}

        for i in range(len(nums)):
            table[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in table and i != table[diff]:
                return [i, table[diff]]
        
        return [0, 0]