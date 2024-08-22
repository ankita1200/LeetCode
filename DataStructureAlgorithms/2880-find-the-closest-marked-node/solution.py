class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:

        graph = defaultdict(list)
        for src,dest,wt in edges:
            graph[src].append((wt,dest))

        shortestPathAt = [float('inf')] * n
        shortestPathAt[s] = 0
        que = [(0,s)]
        chk = set(marked)

        while que:
            currshortestdist, currnode = heapq.heappop(que)
            if currnode in chk:
                return currshortestdist
            for wt,neighbor in graph[currnode]:
                possibledist = currshortestdist + wt
                if shortestPathAt[neighbor] > possibledist:
                    shortestPathAt[neighbor] = possibledist
                    heapq.heappush(que,(possibledist,neighbor))
        
        return -1

        
