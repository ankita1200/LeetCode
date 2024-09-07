class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        que = deque()
        for node in range(n):
            que.append((node,1<<node))
        
        ending_mask = (1 << n) - 1
        visited = set(que)
        steps = 0
        while que:
            quesize = len(que)
            for i in range(quesize):
                node,mask = que.popleft()
                for neighbor in graph[node]:
                    nxt_mask = mask | (1<<neighbor)
                    if nxt_mask == ending_mask:
                        return 1+steps
                    if not (neighbor,nxt_mask) in visited:
                        visited.add((neighbor,nxt_mask))
                        que.append((neighbor,nxt_mask))
            steps += 1

        
