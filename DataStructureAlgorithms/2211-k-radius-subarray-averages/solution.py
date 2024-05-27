class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n<(2*k+1):
            return [-1]*n
        ans=[-1]*n
        i=0
        j=2*k+1
        st=k
        currwin=sum(nums[:j])
        ans[st]=currwin // (2*k+1)
        while j<n:
            currwin+=-nums[i]+nums[j]
            ans[st+1]=currwin//(2*k+1)
            i+=1
            j+=1
            st+=1
        return ans
        
