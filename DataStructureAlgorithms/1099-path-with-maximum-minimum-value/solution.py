class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        minsofar = float('inf')
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        heap = [(-grid[0][0],0,0)] 
        while heap:
            score,x,y = heapq.heappop(heap)
            minsofar = min(minsofar,-score)
            visited[x][y] = True
            if (x == m-1) and (y == n-1):
                break
            for dx,dy in dirs:
                newx = x + dx
                newy = y + dy
                if (0<=newx<m) and (0<=newy<n) and (not visited[newx][newy]):
                    heapq.heappush(heap,(-grid[newx][newy],newx,newy))
        
        return minsofar

        
        
        
