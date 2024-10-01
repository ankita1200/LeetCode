class Solution:

    def __init__(self, nums: List[int]):
        self.ds = {}
        for i in range(len(nums)):
            if nums[i] in self.ds:
                self.ds[nums[i]].append(i)
            else:
                self.ds[nums[i]] = deque([i])
        
    def pick(self, target: int) -> int:
        ele = self.ds[target].popleft()
        self.ds[target].append(ele)
        return ele
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
