class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            return False
        
        seen = set()
        return dfs(source)
        
