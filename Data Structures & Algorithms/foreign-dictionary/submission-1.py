class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        lexical = defaultdict(set)
        indeg = defaultdict(int)

        for word in words:
            for ch in word:
                indeg[ch] = 0

        # building the graph
        for i in range(1, len(words)):
            a, b = words[i-1], words[i]

            while a and b and a[0] == b[0]:
                a = a[1:]
                b = b[1:]
            
            if a and not b:
                return ""
            
            elif a and b:
                lexical[a[0]].add(b[0])
        
        # topological sort

        for key, val in lexical.items():
            for i in val:
                indeg[i] += 1
        

        res, q = "", [key for key, value in indeg.items() if value == 0]

        while q:
            curr = q.pop(0)
            res += curr

            for neighbor in lexical[curr]:
                indeg[neighbor] -= 1

                if indeg[neighbor] == 0:
                    q.append(neighbor)

        for k, v in indeg.items():
            if v:
                return ""

        return res