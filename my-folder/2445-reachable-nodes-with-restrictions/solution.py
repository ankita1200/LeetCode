from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph =defaultdict(list)
        seen = set()
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    self.visits +=1
                    dfs(neighbor)
        
        seen.add(0)
        self.visits = 1
        for node in restricted:
            seen.add(node)
        dfs(0)
        return self.visits
        
