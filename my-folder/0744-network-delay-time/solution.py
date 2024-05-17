class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #represent graph as adjacency list for easy access to neighbor vertices
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))
        
        #use visited array to keep track of visited and non-visited nodes
        visited=[False]*(n+1)
        visited[0]=True
        
        #use an array to keep track of minimum distance to the nodes
        min_dist=[float('inf')]*(n+1)
        min_dist[0]=min_dist[k]=0
        
        #use a minimum heap ds to get the next vertex with minimum distance at each iterration
        pq=[(0,k)]
        while pq:
            dist,node=heapq.heappop(pq)
            if not visited[node]:
                for nx_node in graph[node]:
                    dest_dist, dest_node=nx_node
                    if not visited[dest_node]:
                        min_dist[dest_node]=min(min_dist[dest_node],dist+dest_dist)
                        heapq.heappush(pq,(min_dist[dest_node], dest_node))
                visited[node]=True
                
        return max(min_dist) if float('inf') not in min_dist else -1
        
        
        
        
