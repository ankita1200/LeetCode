# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(node,lowerlimit,upperlimit):
            if not node:
                return True
            if node.val <= lowerlimit or node.val >= upperlimit:
                return False
            left_tree = bst(node.left, lowerlimit, node.val)
            right_tree = bst(node.right, node.val, upperlimit)
            return left_tree and right_tree
        
        return bst(root, float('-inf'), float('inf'))
        
