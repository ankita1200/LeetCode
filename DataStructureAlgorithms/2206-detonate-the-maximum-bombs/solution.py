class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph=defaultdict(list)
        n=len(bombs)
        for i in range(n):
            a1,b1,r1 = bombs[i]
            for j in range(i+1,n):
                a2,b2,r2 = bombs[j]
                dist = (a1-a2)**2 + (b1-b2)**2
                if dist <= r1**2:
                    graph[i].append(j)
                if dist <= r2**2:
                    graph[j].append(i)
        
        def bfs(bomb):
            count=0
            seen = set()
            que = deque([bomb])
            seen.add(bomb)
            while que:
                size = len(que)
                for _ in range(size):
                    bombindex = que.popleft()
                    count+=1
                    for neighbor in graph[bombindex]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            que.append(neighbor)
            return count
        
        ans=0
        for i in range(len(bombs)):
            ans=max(ans,bfs(i))
        return ans
        
