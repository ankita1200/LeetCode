# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        result=0
        def dfs(node):
            nonlocal result
            if not node:
                return 0,0
            leftsum,leftcount=dfs(node.left)
            rightsum,rightcount=dfs(node.right)
            nodesum= node.val+leftsum+rightsum
            nodecount=leftcount+rightcount+1
            if nodesum//nodecount == node.val:
                result+=1
            return nodesum,nodecount

        dfs(root)
        return result
        
