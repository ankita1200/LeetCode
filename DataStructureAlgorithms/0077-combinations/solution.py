class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(curr, first_num):
            if len(curr) == k:
                ans.append(list(curr))
                return
            
            for i in range(first_num,n+1):
                curr.append(i)
                helper(curr,i+1)
                curr.pop()
        
        ans = []
        helper([],1)
        return ans
        
