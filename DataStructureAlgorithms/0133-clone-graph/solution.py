"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node):
            if not node:
                return
            newnode = Node(node.val,[])
            dicnodes[node.val] = newnode
            for neighbor in node.neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    newnode.neighbors.append(dfs(neighbor))
                else:
                    newnode.neighbors.append(dicnodes[neighbor.val])
            return newnode
            
        seen = set()
        dicnodes = {}
        seen.add(node)
        return dfs(node)
                    
        
        
