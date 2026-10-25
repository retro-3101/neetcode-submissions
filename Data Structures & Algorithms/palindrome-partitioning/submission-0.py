class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def ispalindrome(a):

            if a == "".join(reversed(a)):
                return True
            
            return False
        
        def dfs(res, curr, temp):
            
            if not curr:
                if temp:
                    res.append(temp.copy())
                return
            
            for i in range(1, len(curr)+1):
                
                if ispalindrome(curr[:i]):
                    temp.append(curr[:i])
                    dfs(res, curr[i:], temp)
                    temp.pop()
            
            return
        
        dfs(res, s, [])

        return res