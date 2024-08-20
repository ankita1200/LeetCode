class UnionFind:
    def __init__(self,n):
        self.group=[i for i in range(n+1)]
        self.rank=[1] * (n+1)

    def find(self,node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.group[rooty]=rootx
            elif self.rank[rooty]>self.rank[rootx]:
                self.group[rootx]=rooty
            else:
                self.group[rooty]=rootx
                self.rank[rootx] += 1
            return True
        else:
            return False

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf=UnionFind(n)
        connections.sort(key=lambda x: x[2])
        mincost=0
        countedges=0
        for x,y,cost in connections:
            if uf.union(x,y):
                mincost+=cost
                countedges += 1
                if countedges == n-1:
                    break
        
        return mincost if countedges==n-1 else -1
        
        
