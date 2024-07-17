# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves=0
        def distribute(node):
            if node is None:
                return 0

            leftbal=distribute(node.left)
            rightbal=distribute(node.right)
            self.moves+=abs(leftbal)+abs(rightbal)
            return leftbal+rightbal+node.val-1
        
        distribute(root)
        return self.moves



        
