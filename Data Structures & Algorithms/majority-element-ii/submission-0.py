class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        n = len(nums)

        print(count)

        return [key for key, value in count.items() if value > n//3]