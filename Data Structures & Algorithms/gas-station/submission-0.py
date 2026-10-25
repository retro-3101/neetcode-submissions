class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        g, c = 0, 0
        st = 0

        for i in range(len(gas)):
            g += gas[i]
            c += cost[i]

            if g >= c:
                continue
            
            g, c = 0, 0

            st = i+1
        
        if sum(gas) < sum(cost):
            return -1
        
        return st