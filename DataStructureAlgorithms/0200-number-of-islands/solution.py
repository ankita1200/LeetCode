class UnionFind:
    def __init__(self,grid):
        nr,nc = len(grid),len(grid[0])
        self.parent = []
        self.rank = [] 
        self.count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    self.parent.append(i*nc+j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
    
    def getcount(self):
        return self.count
            
    
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        nrows,ncols = len(grid),len(grid[0])
        uf = UnionFind(grid)
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    grid[i][j]="0"
                    if i-1 >=0 and grid[i-1][j]=="1":
                        uf.union(i*ncols+j, (i-1)*ncols+j)
                    if i+1< nrows and grid[i+1][j]=="1":
                        uf.union(i*ncols+j, (i+1)*ncols+j)
                    if j-1 >=0 and grid[i][j-1]=="1":
                        uf.union(i*ncols+j,i*ncols+j-1)
                    if j+1 < ncols and grid[i][j+1]=="1":
                        uf.union(i*ncols+j, i*ncols+j+1)
                        
        return uf.getcount()
                        
        
