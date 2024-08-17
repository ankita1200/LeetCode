# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        que = deque([root])
        while que:
            level=len(que)
            levelsum = 0
            for _ in range(level):
                node = que.popleft()
                levelsum +=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(levelsum/level)
        return ans
        
