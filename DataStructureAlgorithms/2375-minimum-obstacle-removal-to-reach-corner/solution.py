class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        #use bfs and minheap.Minheap to prioritize the path with minimum obstacles
        m=len(grid)
        n=len(grid[0])
        
        def checkValid(row,col):
            return 0<=row<m and 0<=col<n and (row,col) not in seen
        
        seen=set()
        minheap=[(0,0,0)]
        seen.add((0,0))
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        while minheap:
            currPathOb,currRow,currCol=heapq.heappop(minheap)
            if currRow==m-1 and currCol==n-1:
                return currPathOb
            for dx,dy in dirs:
                nextRow=currRow+dx
                nextCol=currCol+dy
                if checkValid(nextRow,nextCol):
                    seen.add((nextRow,nextCol))
                    if grid[nextRow][nextCol]==0:
                        heapq.heappush(minheap,(currPathOb,nextRow,nextCol))
                    else:
                        heapq.heappush(minheap,(currPathOb+1,nextRow,nextCol))
        

        
