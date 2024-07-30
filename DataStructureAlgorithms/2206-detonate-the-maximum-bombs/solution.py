class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        n=len(bombs)
        for i in range(n):
            for j in range(i+1,n):
                dist=(bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2
                if bombs[i][2]**2 >= dist:
                    graph[i].append(j)
                if bombs[j][2]**2 >= dist:
                    graph[j].append(i)
        
        def bfs(bomb_index):
            queue=deque([bomb_index])
            count=0
            seen=set()
            seen.add(bomb_index)
            while queue:
                index=queue.popleft()
                count+=1
                for neighbor in graph[index]:
                    if not neighbor in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
                        
            return count
        
        ans=0
        for index in range(n):
            ans=max(ans,bfs(index))
        return ans

        


        
