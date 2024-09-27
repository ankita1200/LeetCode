class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        n = len(nums)
        for i in range(n):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        result = [0]*n
        st = 0
        for i in range(0,n,2):
            result[i] = even[st]
            st += 1
        st = 0
        for i in range(1,n,2):
            result[i] = odd[st]
            st += 1
        return result

        
