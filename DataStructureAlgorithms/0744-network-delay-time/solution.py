class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src,dest,time in times:
            graph[src].append((time,dest))
        
        for node,neighbors in graph.items():
            neighbors.sort(key = lambda x : x[0])
        
        signalReceivedAt = [float('inf')] * (n+1)
        signalReceivedAt[0] = -1
        signalReceivedAt[k]=0
        que = [(0,k)]
        heapq.heapify(que)
        while que:
            currtime, node = heapq.heappop(que)
            for time,neighbor in graph[node]:
                timetoneighbor = time+currtime
                if signalReceivedAt[neighbor]>timetoneighbor:
                    signalReceivedAt[neighbor]= timetoneighbor
                    heapq.heappush(que,(timetoneighbor,neighbor))
        
        if any(signal == float('inf') for signal in signalReceivedAt):
            return -1
        return max(signalReceivedAt)
