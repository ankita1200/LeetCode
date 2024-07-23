class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp=[]
        for trip in trips:
            timestamp.append([trip[1],trip[0]])
            timestamp.append([trip[2], -trip[0]])
        timestamp.sort()
        curr=0
        for time,passenger_change in timestamp:
            curr+=passenger_change
            if curr>capacity:
                return False
        return True
        
