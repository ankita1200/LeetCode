class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prev = [float('inf')] * n
        curr = [float('inf')] * n
        curr[src] = 0
        
        graph = defaultdict(list)
        for sr,dest,cost in flights:
            graph[dest].append((cost,sr))
        
        
        for _ in range(k+2):
            for dest in range(n):
                for cost,sr in graph[dest]:
                    curr[dest] = min(curr[dest],prev[sr]+cost)
            for i in range(n):
                prev[i]=curr[i]
            
                
        return curr[dst] if curr[dst]!= float('inf') else -1
        
        
