class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        if m==0:
            return 0
        
        grid = [[0]*(n+2) for _ in range(m+2)]
        outdegree = [[0]*(n+2) for _ in range(m+2)]
        for i in range(m):
            for j in range(n):
                grid[i+1][j+1] = matrix[i][j]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                for dx,dy in dirs:
                    x,y = i+dx, j+dy
                    if grid[x][y] > grid[i][j]:
                        outdegree[i][j] += 1
        que = deque()
        for i in range(1,m+1):
            for j in range(1,n+1):
                if outdegree[i][j] == 0:
                    que.append((i,j))
        
        height = 0
        while que:
            height +=1
            size = len(que)
            for _ in range(size):
                i,j = que.popleft()
                for dx,dy in dirs:
                    x,y = i+dx, j+dy
                    if grid[x][y]<grid[i][j]:
                        outdegree[x][y] -= 1
                        if outdegree[x][y] == 0:
                            que.append((x,y))
                            
        return height
                    
                
        
