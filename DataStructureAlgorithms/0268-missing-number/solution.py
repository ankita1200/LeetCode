class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        num_set = set(nums)
        for number in range(l+1):
            if number not in num_set:
                return number
            
        
