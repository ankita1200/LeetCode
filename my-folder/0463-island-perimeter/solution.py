class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dir=[(-1,0),(0,-1),(1,0),(0,1)]
        def checkwater(x,y):
            return x<0 or x>=m or y<0 or y>=n or grid[x][y]==0
        
        def bfs(x,y):
            nonlocal perimeter
            seen.add((x,y))
            for dx,dy in dir:
                newx=x+dx
                newy=y+dy
                iswater= checkwater(newx,newy)
                if iswater:
                    perimeter+=1
                if not iswater and (newx,newy) not in seen:
                    bfs(newx,newy)
            
        perimeter=0
        seen=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    bfs(i,j)
                    return perimeter
        
        
