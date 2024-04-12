class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        if n <= 1:
            return graph
        
        end = n-1
        paths = []
        def bfs(node, path):
            if node == end:
                paths.append(list(path))
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                bfs(neighbor, path)
                path.pop()
            
            
        bfs(0, [0])
        return paths
        
