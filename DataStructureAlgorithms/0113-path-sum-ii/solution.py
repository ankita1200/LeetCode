# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, prevsum, prevpath):
            if not node:
                return
            
            currsum = prevsum + node.val
            currpath = prevpath + [node.val]
            if (not node.left) and (not node.right) and (currsum == targetSum):
                self.ans.append(currpath)
                return
            dfs(node.left, currsum, currpath)
            dfs(node.right, currsum, currpath)
        
        self.ans = []
        dfs(root, 0, [])
        return self.ans

        
