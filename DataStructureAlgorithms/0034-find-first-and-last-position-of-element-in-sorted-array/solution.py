class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowerbound=self.findBound(nums,target,True)
        if lowerbound==-1:
            return [-1,-1]
        upperbound=self.findBound(nums,target,False)
        return [lowerbound, upperbound]

    def findBound(self, nums, target, isFirst):
        n=len(nums)
        begin, end = 0, n-1
        while begin<=end:
            mid=(begin+end) //2
            if nums[mid]==target:
                if isFirst:
                    if mid==begin or nums[mid-1]<target:
                        return mid
                    else:
                        end=mid-1
                else:
                    if mid==end or nums[mid+1]>target:
                        return mid
                    else:
                        begin=mid+1
            elif nums[mid]< target:
                begin=mid+1
            else:
                end=mid-1
        return -1
