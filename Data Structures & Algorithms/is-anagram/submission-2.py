class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sdict = {}
        tdict = {}

        for ch in s:
            sdict[ch] = 1 + sdict.get(ch, 0)
        
        for ch in t:
            tdict[ch] = 1 + tdict.get(ch, 0)
        
        return sdict == tdict