class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # build graph
        n=len(original)
        graph=defaultdict(list)
        for i in range(n):
            graph[original[i]].append((changed[i],cost[i]))
        
        @cache
        def shortestPath(src,tar):
            pq=[(0,src)]
            seen=set()
            while pq:
                currCost,node=heapq.heappop(pq)
                if node==tar:
                    return currCost
                for neighbor,wt in graph[node]:
                    if neighbor not in seen:
                        heapq.heappush(pq,(currCost+wt,neighbor))
                seen.add(node)
            return -1

        size=len(source)
        cost=0
        for pos in range(size):
            if source[pos]!=target[pos]:
                val= shortestPath(source[pos],target[pos])
                if val==-1:
                    return -1
                else:
                    cost+=val
        return cost
        
