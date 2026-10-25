class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mx = dict()

        for i, ch in enumerate(s):
            mx[ch] = i
        
        res = [mx[s[0]]]

        for i in range(1, len(s)):

            if res[-1] >= i:
                res[-1] = max(res[-1], mx[s[i]])
            
            else:
                res.append(mx[s[i]])
        
        for i in range(len(res)-1, 0, -1):
            res[i] = res[i] - res[i-1]
        
        res[0]+=1

        return res
