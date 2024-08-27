class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probabs = [0]*n
        graph = defaultdict(list)
        for index,edge in enumerate(edges):
            prob = succProb[index]
            graph[edge[0]].append((edge[1],prob))
            graph[edge[1]].append((edge[0],prob))
        
        que = [(-1,start_node)]
        while que:
            prob,node = heapq.heappop(que)
            for neighbor,nextprob in graph[node]:
                if probabs[neighbor] < (-prob*nextprob):
                    probabs[neighbor]=-prob*nextprob
                    heapq.heappush(que,(prob*nextprob,neighbor))
        
        return probabs[end_node]
        
