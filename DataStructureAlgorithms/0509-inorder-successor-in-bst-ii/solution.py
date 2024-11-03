"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return
        
        def traverse(nnode):
            if not nnode:
                return
            if not nnode.left and not nnode.right:
                return nnode
            ans = traverse(nnode.left)
            if ans:
                return ans
            return nnode
        
        def getparent(pnode,val):
            if not pnode:
                return
            if pnode.val>val:
                return pnode
            return getparent(pnode.parent,val)

        # first check for right tree. The first leaf will be successor
        succ = traverse(node.right)
        if succ:
            return succ
        # check parent
        return getparent(node.parent,node.val)
