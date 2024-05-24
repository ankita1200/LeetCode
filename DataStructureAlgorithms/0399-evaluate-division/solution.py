class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #build graph
        graph=defaultdict(list)
        size=len(values)
        
        def bfs(start,dest):
            seen=set()
            que=deque([(start,1)])
            seen.add(start)
            while que:
                node,val=que.popleft()
                if node==dest:
                    return val
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        que.append([neighbor[0],val*neighbor[1]])
            return -1
        
        ans=[]
        for i in range(size):
            a,b=equations[i]
            value=values[i]
            graph[a].append((b,value))
            graph[b].append((a,1/value))

        variables=graph.keys()
        n=len(queries)
        for i in range(n):
            startnode,destnode=queries[i]
            print(f"start:{startnode}, dest:{destnode}")
            if startnode not in variables or destnode not in variables:
                ans.append(-1)
                continue
            if startnode==destnode:
                ans.append(1.0)
                continue
            fin=bfs(startnode,destnode)
            ans.append(fin)
        return ans
            
                


        
