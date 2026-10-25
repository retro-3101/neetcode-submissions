class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        def dfs(temp, cursum, i):
            
            if cursum == target:
                print('here')
                res.add(tuple(temp.copy()))
                return

            if i>=n or cursum > target:
                return

            temp.append(nums[i])

            dfs(temp, cursum+nums[i], i)

            temp.pop()

            dfs(temp, cursum, i+1)

            return
        
        dfs([], 0, 0)
        
        return [list(val) for val in res]

            

            
