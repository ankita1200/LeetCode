# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def bst(node):
            if not node:
                return
            if target == node.val:
                self.closest = node.val
                self.minval = 0
                return
            chk = abs(target-node.val)
            if chk == self.minval:
                self.closest = min(self.closest, node.val)
            if chk < self.minval:
                self.closest = node.val
                self.minval = chk
            
            if target < node.val:
                bst(node.left)
                return
            bst(node.right)
                
        self.minval = float('inf')
        self.closest = 0
        bst(root)
        return self.closest
        
