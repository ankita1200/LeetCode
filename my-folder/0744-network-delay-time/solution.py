class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))
        
        visited=[False]*(n+1)
        visited[0]=True
        min_dist=[float('inf')]*(n+1)
        pq=[]
        min_dist[0]=min_dist[k]=0
        for node in graph[k]:
            dist,dest=node
            pq.append(node)
            min_dist[dest]=dist
        heapq.heapify(pq)
        visited[k]=True
        count=n-1
        while pq and count>0:
            dist,node=heapq.heappop(pq)
            if not visited[node]:
                visited[node]=True
                for nx_node in graph[node]:
                    dest_dist, dest_node=nx_node
                    if not visited[dest_node]:
                        min_dist[dest_node]=min(min_dist[dest_node],dist+dest_dist)
                        heapq.heappush(pq,(min_dist[dest_node], dest_node))
                count-=1
        return max(min_dist) if float('inf') not in min_dist else -1
        
        
        
        
