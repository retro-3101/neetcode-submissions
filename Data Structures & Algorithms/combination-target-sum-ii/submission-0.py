class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = set()

        def dfs(temp, cursum, i):
            
            if cursum == target:
                print('here')
                res.add(tuple(temp.copy()))
                return

            if i>=n or cursum > target:
                return

            temp.append(candidates[i])

            dfs(temp, cursum + candidates[i], i+1)

            temp.pop()

            dfs(temp, cursum, i+1)

            return
        
        dfs([], 0, 0)
        
        return [list(val) for val in res]
