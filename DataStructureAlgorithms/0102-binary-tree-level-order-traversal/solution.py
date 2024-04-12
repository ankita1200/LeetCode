# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            #number of nodes at current level
            nodes=len(queue)
            level=[]
            for _ in range(nodes):
                node=queue.popleft()
                level.append(node.val)
                # queue gets updated. So does its length
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans



        
