class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if len(manager)==1:
            return 0
        graph=defaultdict(list)
        for index,emp in enumerate(manager):
            if emp!=-1:
                graph[emp].append(index)
        
        def dfs(node,val):
            if not graph[node]:
                self.maxval=max(self.maxval,val)
            for neighbor in graph[node]:
                dfs(neighbor,val+informTime[node])
            return
        
        self.maxval=0
        dfs(headID,0)
        return self.maxval
