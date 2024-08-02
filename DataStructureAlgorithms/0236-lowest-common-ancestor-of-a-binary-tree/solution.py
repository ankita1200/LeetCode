# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(node):
            if not node:
                return
            if node==p:
                return p
            if node==q:
                return q
            
            left=traversal(node.left)
            right=traversal(node.right)
            if (left==p and right==q) or (left==q and right==p):
                return node
            return left or right
            
        return traversal(root)
