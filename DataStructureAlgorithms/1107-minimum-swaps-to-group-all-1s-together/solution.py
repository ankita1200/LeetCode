class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        for n in data:
            if n==1:
                ones += 1
        if ones==0:
            return 0
        left = 0
        zeros = 0
        ans = float('inf')
        for right in range(len(data)):
            if data[right]==0:
                zeros += 1
            if right-left+1==ones:
                ans = min(ans,zeros)
                if data[left]==0:
                    zeros -= 1
                left += 1
        return ans

        
