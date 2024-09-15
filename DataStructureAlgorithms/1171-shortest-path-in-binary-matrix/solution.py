class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if not grid or grid[0][0]==1:
            return -1
        dirs = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        que = deque([(0,0,1)])
        grid[0][0]=1
        while que:
            size = len(que)
            for _ in range(size):
                x,y,dist = que.popleft()
                if x==n-1 and y==n-1:
                    return dist
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if (0<=nx<n) and (0<=ny<n) and grid[nx][ny]==0:
                        grid[nx][ny]=1
                        que.append((nx,ny,dist+1))
                
        return -1
                        
                
                
        
        
