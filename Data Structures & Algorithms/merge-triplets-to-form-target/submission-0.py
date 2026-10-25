class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = [False]*3

        for triplet in triplets:

            if all([triplet[i] <= target[i] for i in range(3)]):

                for i in range(3):
                    res[i] = res[i] or (triplet[i] == target[i])

        return all(res)