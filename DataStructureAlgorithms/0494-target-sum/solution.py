class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        @cache
        def buildExp(pos,sumval):
            if pos==len(nums)-1 and sumval==target:
                return 1
            if pos==len(nums)-1 and sumval!=target:
                return 0
            if pos>=len(nums):
                return 0
            
            return buildExp(pos+1,sumval+nums[pos+1])+buildExp(pos+1,sumval-nums[pos+1])
        return buildExp(0,nums[0])+buildExp(0,-nums[0])
            
        
