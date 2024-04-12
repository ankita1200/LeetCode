class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def func(curr,pos):
            if sum(curr) == n and len(curr) == k:
                ans.append(list(curr))
                return
            if sum(curr) > n or len(curr) == k:
                return 
            for i in range(pos,10):
                curr.append(i)
                func(curr, i+1)
                curr.pop(curr.index(i))
            
        ans = []
        func([],1)
        return ans
        
