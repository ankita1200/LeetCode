# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        que=deque()
        que.append(root)
        result=[]
        while que:
            result.append(que[-1].val)
            n=len(que)
            for i in range(n):
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result

        
