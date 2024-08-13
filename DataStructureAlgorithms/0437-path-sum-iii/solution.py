# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def preorder(node, currsum):
            if not node:
                return
            currsum += node.val
            if currsum == targetSum:
                self.count += 1
            self.count += h[currsum-targetSum]
            h[currsum] += 1
            preorder(node.left, currsum)
            preorder(node.right, currsum)
            h[currsum] -= 1

        
        h = defaultdict(int)
        self.count = 0
        preorder(root, 0)
        return self.count
                
        
