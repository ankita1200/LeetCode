
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def buildTree(left,right):
            if left > right:
                return
            self.postorder_index -=1
            rootval = postorder[self.postorder_index]
            node = TreeNode(rootval)
            rootindex=inordermap[rootval]
            node.right = buildTree(rootindex+1,right)
            node.left = buildTree(left,rootindex-1)
            return node
        
        self.postorder_index = len(postorder)
        inordermap = {}
        for index,value in enumerate(inorder):
            inordermap[value]=index
        return buildTree(0,len(inorder)-1)
               


