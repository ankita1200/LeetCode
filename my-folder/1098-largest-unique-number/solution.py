class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts=defaultdict(int)
        for num in nums:
            counts[num]+=1
        d={k:v for k,v in counts.items() if v==1}
        if d:
            return max(d.keys())
        else:
            return -1
        
