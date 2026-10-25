class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sdict = defaultdict(int)
        tdict = defaultdict(int)

        for ch in s:
            sdict[ch] += 1
        
        for ch in t:
            tdict[ch] += 1
        
        if(sdict == tdict):
            return True
        
        return False