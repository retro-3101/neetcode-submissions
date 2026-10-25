class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.out = []

        self.selector(nums, [])

        return self.out
    
    def selector(self, nums: List[int], res: List[int]) -> None:

        if not nums:
            self.out.append(res.copy())
            return
        
        self.selector(nums[1:], res)

        res.append(nums[0])

        self.selector(nums[1:], res)
        res.pop()

        return