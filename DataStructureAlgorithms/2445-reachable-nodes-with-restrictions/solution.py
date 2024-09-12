from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = [False] * n
        lookup = set(restricted)

        def dfs(node):
            if seen[node] or node in lookup:
                return
            seen[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)
        
        dfs(0)
        return sum(seen)
            

        
