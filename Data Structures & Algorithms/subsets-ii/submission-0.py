class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        res.add(())

        def helper(rest, temp, m):
            
            if m==0:
                return

            for i in range(m):
                temp.append(rest[i])
                temp.sort()
                res.add(tuple(temp.copy()))
                helper(rest[0:i]+rest[i+1:], temp, m-1)
                temp.remove(rest[i])
            
            return
        
        helper(nums, [], len(nums))

        return [list(element) for element in res]
