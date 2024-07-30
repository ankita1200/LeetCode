class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for index,room in enumerate(rooms):
            graph[index]+=room
        
        def dfs(node):
            isVisited[node]=True
            for neighbor in graph[node]:
                if not isVisited[neighbor]:
                    dfs(neighbor)
            return
        
        isVisited=[False]*len(rooms)
        dfs(0)
        return True if sum(isVisited) == len(rooms) else False

        
