class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for x,y in redEdges:
            graph[x].append((y,0))
        for x,y in blueEdges:
            graph[x].append((y,1))
        ans = [-1] * n
        ans[0] = 0
        que = deque()
        seen = set()
        seen.add((0,0))
        seen.add((0,1))
        
        for neighbor,inEdgeColor in graph[0]:
            que.append((neighbor,inEdgeColor, 1))
            seen.add((neighbor,inEdgeColor))
            if neighbor != 0:
                ans[neighbor] = 1
        
        while que:
            currnode,inedge, level = que.popleft()
            for neighbor,outedge in graph[currnode]:
                if (neighbor,outedge) not in seen and inedge != outedge:
                    if ans[neighbor] == -1:
                        ans[neighbor] = level + 1
                    seen.add((neighbor,outedge))
                    que.append((neighbor,outedge,level+1))
        return ans

        
