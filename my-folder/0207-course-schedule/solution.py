class Solution:
    def dfs(self, node, visited, inStack, graph):
        if inStack[node]:
            return False
        if visited[node]:
            return True
        visited[node] = True
        inStack[node] = True
        for neighbor in graph[node]:
            val = self.dfs(neighbor, visited, inStack, graph)
            if not val:
                return False
        inStack[node] = False
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        visited = [False] * numCourses
        inStack = [False] * numCourses
        graph = [[] for _ in range(numCourses)]
        for cond in prerequisites:
            graph[cond[1]].append(cond[0])
        for node in range(numCourses):
                if not self.dfs(node, visited, inStack, graph):
                    return False
        return True

    

        
        
