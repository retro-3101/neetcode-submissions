class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        dp = [0]*(n)

        for i in range(0, n):

            if i==0:
                pass
            
            elif dp[i-1]==0:
                continue

            for word in wordDict:
                m = len(word)

                if i+m<=n and s[i:i+m] == word:
                    dp[i+m-1] = 1
        
        print(dp)
        return bool(dp[n-1])
