# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_dia = 0
        def helper(node):
            if not node:
                return 0
            nonlocal max_dia
            left = helper(node.left)
            right = helper(node.right)
            max_dia = max(max_dia, left+right)
            return max(left, right)+1
        helper(root)
        return max_dia
