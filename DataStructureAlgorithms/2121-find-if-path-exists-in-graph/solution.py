from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        if not edges:
            return False
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node, seen):
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor, seen):
                        return True
            return False
        
        seen=set()
        seen.add(source)
        return dfs(source, seen)
        
