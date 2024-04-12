class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        fin = [0] * n
        curr=n-1
        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                fin[curr]=nums[left]*nums[left]
                left+=1
            else:
                fin[curr]=nums[right]*nums[right]
                right-=1
            curr-=1
        return fin
                
        
