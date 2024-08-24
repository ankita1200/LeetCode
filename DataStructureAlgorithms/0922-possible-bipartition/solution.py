class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = [-1] * (n+1)
        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(source):
            que = deque([source])
            group[source] = 0
            while que:
                node = que.popleft()
                for neighbor in graph[node]:
                    if group[neighbor]==group[node]: return False
                    if group[neighbor]==-1:
                        group[neighbor] = 1-group[node]
                        que.append(neighbor)
            return True
        for node in range(1,n+1):
            if group[node] == -1:
                if not bfs(node):
                    return False
        return True
        
        
