class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader=0
        writer=0
        val=nums[0]
        n=len(nums)
        while reader<n:
            if nums[reader] != val:
                val=nums[reader]
                writer=writer+1
                nums[writer]=nums[reader]
            reader+=1
        print(nums)
        return writer+1
        
