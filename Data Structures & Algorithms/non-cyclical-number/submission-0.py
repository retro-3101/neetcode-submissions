class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:

            num = str(n)
            n = 0
            for digit in num:
                n += (int(digit))**2
            
            if n in seen:
                return False
            seen.add(n)
        
        return True

