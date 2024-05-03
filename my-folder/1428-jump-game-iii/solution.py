class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        def checkValid(pos):
            return 0<=pos<n
        
        def dfs(index):
            if arr[index]==0:
                return True
            if index in seen:
                return False
            seen.add(index)
            if checkValid(index+arr[index]) and dfs(index+arr[index]):
                return True
            if checkValid(index-arr[index]) and dfs(index-arr[index]):
                return True
            return False
        
        seen=set()
        return dfs(start)
                
                
            
        
