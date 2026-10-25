class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        maxn = 0
        n = len(s)
        for i in range(n):
            
            j = 0
            while i-j >= 0 and i+j<n and s[i-j] == s[i+j]:
                if 2*j+1 > maxn:
                    res = s[i-j:i+j+1]
                    maxn = 2*j+1
                j+=1
            
            j = 0
            while i-j >= 0 and i+j+1 < n and s[i-j] == s[i+1+j]:

                if (1+j)*2 > maxn:
                    res = s[i-j: i+j+2]
                    maxn = (1+j)*2
                j+=1
        return res
