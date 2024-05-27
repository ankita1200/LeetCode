class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k >= n:
            return n
        left=right=0
        counter=0
        maxlen=0
        while right<n:
            if nums[left]==0 and nums[right]==0 and left==right:
                left+=1
                right+=1
            elif nums[right]==1:
                right+=1
            elif nums[right]==0 and counter<k:
                right+=1
                counter+=1
            else:
                maxlen=max(maxlen,right-left)
                while left<right:
                    if nums[left]==0:
                        left+=1
                        counter-=1
                        break
                    left+=1
        if right==n:
            maxlen=max(maxlen,right-left)
        return maxlen
            

