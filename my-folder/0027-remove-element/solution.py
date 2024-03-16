class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[j]==val:
                j-=1
                continue
            elif nums[i]== val:
                nums[i], nums[j] = nums[j], nums[i]
                j=j-1
                i=i+1
            else:
                i+=1
        return j+1
        
        
