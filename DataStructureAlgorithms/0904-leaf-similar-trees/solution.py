# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.tree1=[]
        self.tree2=[]
        def dfs(node,tree=True):
            if not node:
                return
            if not node.left and not node.right:
                if tree:
                    self.tree1.append(node.val)
                else:
                    self.tree2.append(node.val)
            dfs(node.left,tree)
            dfs(node.right,tree)
        
        dfs(root1)
        dfs(root2,False)
        return True if self.tree1==self.tree2 else False
        
