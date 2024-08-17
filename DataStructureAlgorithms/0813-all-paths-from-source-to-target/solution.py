class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        self.ans = []
        def dfs(path):
            if path[-1] == n-1:
                self.ans.append(path)
                return
            node = path[-1]
            
            for neighbor in graph[node]:
                if neighbor not in path:
                    newpath = path + [neighbor]
                    dfs(newpath)
        
        dfs([0])
        return self.ans
                    
            
        
