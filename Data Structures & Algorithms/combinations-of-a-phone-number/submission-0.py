class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mp = {
            "2": ["a", "b", "c"], 
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []

        n = len(digits)

        def dfs(res, curr, i, n, digits) -> None:

            if i==n:
                if curr:
                    res.append(curr)
                return
            
            for val in mp[digits[i]]:
                dfs(res, curr+val, i+1, n, digits)
            
            return
        
        dfs(res, "", 0, n, digits)
        return res
                