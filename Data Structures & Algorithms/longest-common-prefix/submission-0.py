class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minlen = len(strs[0])

        for s in strs:
            minlen = min(len(s), minlen)
        
        res = strs[0][:minlen]
        n = len(res)

        for s in strs[1:]:
            while res != s[:n]:
                res = res[:-1]
                n-=1
        
        return res