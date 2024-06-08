class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        start=count=0
        while count<n:
            curr,prev=start,nums[start]
            while True:
                nextpos=(curr+k)%n
                nums[nextpos],prev=prev,nums[nextpos]
                curr=nextpos
                count+=1
                if start==curr:
                    break
            start+=1
            
        


        
