# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node,skip):
            if not node:
                return 0
            money = 0
            if not skip:
                money =node.val+ dp(node.left,True)+ dp(node.right,True)
            else: 
                money = max(dp(node.left,False),dp(node.left,True)) + max(dp(node.right,False),dp(node.right,True))
            return money
        
        return max(dp(root,True),dp(root,False))

        
