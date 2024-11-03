class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2!=0:
            return False
        chksum = tot/2

        @cache
        def partition(i,currsum):
            if i==len(nums):
                return currsum==chksum
            return partition(i+1,currsum+nums[i]) or partition(i+1,currsum)

        return partition(0,0)
            
            
        
