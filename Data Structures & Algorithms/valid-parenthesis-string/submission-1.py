class Solution:
    def checkValidString(self, s: str) -> bool:
        mn, mx = 0, 0

        for ch in s:

            if ch == "(":
                mn, mx = mn+1, mx+1
            
            elif ch == ")":
                mn, mx = mn-1, mx-1
            
            else:
                mn, mx = mn-1, mx+1
            
            if mx < 0:
                return False
            if mn < 0:
                mn = 0

        return mn == 0