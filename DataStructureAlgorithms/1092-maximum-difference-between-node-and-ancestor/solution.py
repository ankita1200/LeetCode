# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        
        def dfs(node, minval, maxval):
            if not node:
                return
            minval = min(minval, node.val)
            maxval = max(maxval, node.val)
            self.ans=max(self.ans, abs(maxval-minval))
            dfs(node.left,minval, maxval)
            dfs(node.right, minval, maxval)
            
        self.ans=0
        dfs(root,root.val,root.val)
        return self.ans
        
        
