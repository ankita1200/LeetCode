# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue=deque([root])
        left=True
        while queue:
            nodes_level = len(queue)
            level=[]
            for _ in range(nodes_level):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left:
                ans.append(level)
                left=False
            else:
                ans.append(level[::-1])
                left=True
                
        return ans
        
