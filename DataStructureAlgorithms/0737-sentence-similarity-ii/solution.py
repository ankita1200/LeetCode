class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        words = set()
        for word1,word2 in similarPairs:
            words.add(word1)
            words.add(word2)
        words = list(words)
        indexes = {}
        for index,word in enumerate(words):
            indexes[word] = index
        uf = UnionFind(len(words))
        for word1,word2 in similarPairs:
            uf.union(indexes[word1],indexes[word2])
        for worda,wordb in zip(sentence1,sentence2):
            if (worda==wordb) or ((worda in words) and (wordb in words) ) and (uf.checksimilar(indexes[worda],indexes[wordb])):
                continue
            else:
                return False
        return True
            

class UnionFind:
    def __init__(self,n):
        self.rank = [1] * n
        self.root = [i for i in range(n)]
    
    def find(self,x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            elif self.rank[rooty] < self.rank[rootx]:
                self.root[rooty] = rootx
            else:
                self.root[rooty]=rootx
                self.rank[rootx] += 1
    
    def checksimilar(self,x,y):
        return self.find(x) == self.find(y)
    
            


        
