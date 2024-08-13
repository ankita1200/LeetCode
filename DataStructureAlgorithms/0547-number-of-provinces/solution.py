class QuickFind:
    def __init__(self, size):
        self.size = size
        self.root = [0] * size
        for i in range(size):
            self.root[i] = i
    def find(self, x):
        return self.root[x]
        
    def union(self, x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            for i in range(self.size):
                if self.root[i] == rooty:
                    self.root[i] = rootx

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = QuickFind(n)
        
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return len(set(uf.root))
            
    

