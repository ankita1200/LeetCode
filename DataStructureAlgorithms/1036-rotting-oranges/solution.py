class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        que = deque()
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i,j,0))
                if grid[i][j] == 1:
                    flag = True
        if not que:
            return -1 if flag else 0
        
        time = -1
        while que:
            size = len(que)
            for _ in range(size):
                x,y,time = que.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        que.append((nx,ny,time+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        
        return time
                
        
