class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(stones)):
            x,y = stones[i]
            for j in range(i+1,len(stones)):
                a,b = stones[j]
                if x==a or y==b:
                    graph[(x,y)].append((a,b))
                    graph[(a,b)].append((x,y))
        
        
        def dfs(node):
            self.visited.add(node)
            for neighbor in graph[node]:
                if not neighbor in self.visited:
                    dfs(neighbor)
            return
        
        components = 0
        self.visited = set()
        print(graph)
        for x,y in stones:
            if (x,y) not in self.visited:
                components += 1
                dfs((x,y))
        
        return len(stones) - components


                
        
