class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store.keys():
            self.store[key]=[]
        self.store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""
        if timestamp < self.store[key][0][0]:
            return ""
        left=0
        right=len(self.store[key])
        while left<right:
            mid=(left+right) //2
            if self.store[key][mid][0]<=timestamp:
                left=mid+1
            else:
                right=mid
        return "" if right==0 else self.store[key][right-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
