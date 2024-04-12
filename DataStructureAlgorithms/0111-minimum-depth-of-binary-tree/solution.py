# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ld = 1+ self.minDepth(root.left)
        rd = 1+ self.minDepth(root.right)
        
        if ld == 1:
            return rd
        elif rd == 1:
            return ld
        else:
            return min(ld, rd)
    
    
        
