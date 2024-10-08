class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for city1,city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        maxval = 0
        for node1 in range(n):
            for node2 in range(node1+1,n):
                networkrank=len(graph[node1]) + len(graph[node2])
                if node1 in graph[node2]:
                    networkrank -= 1
                maxval = max(maxval,networkrank)
        return maxval
