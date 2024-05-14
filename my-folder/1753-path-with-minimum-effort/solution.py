class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols=len(heights), len(heights[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        pque=[[0,0,0]]
        visited=set()
        
        while pque:
            diff,r,c=heapq.heappop(pque)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (rows-1,cols-1):
                return diff
            
            for dr,dc in directions:
                newr=r+dr
                newc=c+dc
                if newr<0 or newc<0 or newr==rows or newc==cols or (newr,newc) in visited:
                    continue
                newdiff=max(diff,abs(heights[r][c]-heights[newr][newc]))
                heapq.heappush(pque,[newdiff,newr,newc])
        
            
                
                    
            
       
            
            
        
        
