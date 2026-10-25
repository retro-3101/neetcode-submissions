class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for i in range(len(nums)+1)]

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                if(k > 0):
                    res.append(num)
                    k-=1
                else:
                    break
            
            if(k<=0):
                break

        return res
