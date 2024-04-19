class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = []
        for i in range(len(nums)):
            if nums[i] in d:
                return list((d.index(nums[i]),i))
            d.append(target-nums[i])
        return 
        
