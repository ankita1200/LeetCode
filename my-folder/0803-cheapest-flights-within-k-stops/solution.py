class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges=k+1
        dp = [[float('inf')]*n for i in range(edges+1)]
        for i in range(edges+1):
            dp[i][src]=0
        
        graph=defaultdict(list)
        for sr,de,cost in flights:
            graph[de].append((sr,cost))
            
        for i in range(1,edges+1):
            for j in range(n):
                if j==src:
                    continue
                for source,cost in graph[j]:
                    dp[i][j]=min(dp[i][j],dp[i-1][source]+cost)
        
        return dp[edges][dst] if dp[edges][dst] != float('inf') else -1
                
                
        
