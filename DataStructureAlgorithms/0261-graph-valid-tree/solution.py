class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #using dfs to find if a graph is a tree
        
        graph=defaultdict(list)
        for nodex,nodey in edges:
            graph[nodex].append(nodey)
            graph[nodey].append(nodex)
        nodes=set()
        parent={}
        stack=[0]
        while stack:
            currnode=stack.pop()
            nodes.add(currnode)
            for neighbor in graph[currnode]:
                if parent.get(currnode)==neighbor: continue
                if neighbor in parent: return False
                stack.append(neighbor)
                parent[neighbor]=currnode
        return len(nodes)==n
            
            
        
