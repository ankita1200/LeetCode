class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if min(nums)>0:
            return 1
        prefixsum=[nums[0]]
        for i in range(1,len(nums)):
            prefixsum.append(nums[i]+prefixsum[i-1])
        if min(prefixsum)>0:
            return 1
        else:
            return min(prefixsum)*-1+1 
        
            
