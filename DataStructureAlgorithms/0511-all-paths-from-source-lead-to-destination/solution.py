from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        def dfs(node):
            if self.state[node] == 2:
                return True
            if self.state[node]==1:
                # cycle detected
                return False
            if not graph[node]:
                return node==destination
            self.state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            self.state[node]=2
            return True
        
        self.state = [0] * n
        return dfs(source)
            
        
       
