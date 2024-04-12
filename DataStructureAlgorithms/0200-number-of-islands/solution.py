class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #check validity
        def validity(x,y):
            return 0<=x<m and 0<=y<n and grid[x][y]=="1"

        #use depth first search to explore a component
        def dfs(x,y):
            for dx,dy in steps:
                newX=x+dx
                newY=y+dy
                if validity(newX,newY) and (newX,newY) not in seen:
                    seen.add((newX,newY))
                    dfs(newX,newY)

        
        #counts the number of islands/components
        ans=0
        seen=set()
        #directions- equivalent to locating neighbors
        steps=[(0,1),(1,0),(-1,0),(0,-1)]
        m=len(grid)
        n=len(grid[0])
        
        #Iterate through the matrix to find all the islands
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="0":
                    seen.add((i,j))
                elif (grid[i][j]=="1") and ((i,j) not in seen):
                    seen.add((i,j))
                    ans+=1
                    dfs(i,j)
        
        return ans
                
        
