class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            sz = len(s)
            res = res + str(sz) + '%' + s
        
        return res

    def decode(self, s: str) -> List[str]:

        strs = []

        while len(s):
            parts = s.split('%', 1)

            sz = int(parts[0])
            s = parts[1]
            strs.append(s[0: sz])
            s = s[sz:]
        
        return strs