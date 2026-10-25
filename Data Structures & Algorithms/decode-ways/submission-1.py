class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] * n

        if int(s[0]) != 0:
            dp[0] = 1
        else:
            return 0
        
        if n == 1:
            return dp[0]
        
        a = 1 if int(s[0:2])>9 and int(s[0:2])<27 else 0
        b = 1 if int(s[1])!=0 else 0
        dp[1] = a+b
        
        for i in range(2, n):

            a = dp[i-1] if int(s[i])!=0 else 0

            b = dp[i-2] if int(s[i-1:i+1])>9 and int(s[i-1:i+1])<27 else 0

            dp[i] = a+b
        
        return dp[n-1]
