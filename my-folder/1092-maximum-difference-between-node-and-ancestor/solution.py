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
        self.result = 0
        def helper(node, curr_max, curr_min):
            if not node:
                return
            
            self.result = max(self.result, abs(curr_max-node.val), abs(curr_min - node.val))
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            helper(node.left, curr_max, curr_min)
            helper(node.right, curr_max, curr_min)

        helper(root, root.val, root.val)
        return self.result
            
