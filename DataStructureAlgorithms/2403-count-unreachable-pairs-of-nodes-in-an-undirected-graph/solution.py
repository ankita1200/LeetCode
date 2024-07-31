class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            isVisited.add(node)
            for neighbor in graph[node]:
                if not neighbor in isVisited:
                    dfs(neighbor)

        isVisited=set()
        nodes=[]
        for node in range(n):
            if not node in isVisited:
                curr=len(isVisited)
                dfs(node)
                nodes.append(len(isVisited)-curr)
        x=len(nodes)
        ans=0
        sumnodes=sum(nodes)
        for i in range(x):
            ans+=nodes[i]*(sumnodes-nodes[i])
        return ans//2
