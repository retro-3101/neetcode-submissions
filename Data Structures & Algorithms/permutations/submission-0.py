class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def helper(temp, rest, m):

            if m==0:
                res.append(temp.copy())
                return
            
            for i in range(m):
                temp.append(rest[i])
                helper(temp, rest[0:i]+rest[i+1:], m-1)
                temp.pop()
            
            return
        
        helper([], nums, n)

        return res
            
            