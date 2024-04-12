class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            return 1 + sum([dfs(neighbor) for neighbor in graph[node]])
                
        seen=set(restricted)
        return dfs(0)
        
                
        
                    
