class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start,end in intervals:
            events.append((start,1))
            events.append((end+1,-1))
        maxval = 0 
        prefixsum = 0
        events.sort()
        for point,x in events:
            prefixsum += x
            maxval = max(maxval,prefixsum)
        return maxval
        
        
