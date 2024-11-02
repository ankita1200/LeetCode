class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # minimum value of divisor
        left = 1
        # maximum value of divisor
        right = max(nums)
        print(right)
        
        while left <= right:
            divisor = (left+right) // 2
            result = sum([ceil(n/divisor) for n in nums])
            if result>threshold:
                left = divisor+1
            else:
                right = divisor-1
        return left
                
        
