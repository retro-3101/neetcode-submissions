class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = set()

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1

            while j<k:
                target = nums[i] + nums[j] + nums[k]

                if target == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                
                elif target>0:
                    k-=1
                
                else:
                    j+=1
        
        return list(result)

