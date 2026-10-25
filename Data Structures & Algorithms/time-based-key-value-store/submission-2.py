class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        
        return

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        l, r = 0, len(self.store.get(key, [])) - 1

        while l<=r:
            
            mid = (l+r)//2

            if timestamp >= self.store[key][mid][0]:
                l = mid+1
                res = self.store[key][mid][1]
            else:
                r = mid-1
        
        return res
