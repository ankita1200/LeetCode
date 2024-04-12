class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def findcomb(comb,indx):
            if sum(comb) == target:
                ans.append(list(comb))
                return
            if sum(comb) > target:
                return
            for i in range(indx,l):
                comb.append(candidates[i])
                findcomb(comb,i)
                comb.pop()

        l = len(candidates)
        findcomb([],0)
        return ans
        
