# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        ans = defaultdict(list)
        queue = deque([(root,0)])
        while queue:
            n = len(queue)
            for i in range(n):
                node,col_index = queue.popleft()
                ans[col_index].append(node.val)
                if node.left is not None:
                    queue.append((node.left, col_index-1))
                if node.right is not None:
                    queue.append((node.right,col_index+1))
        return [ans[x] for x in sorted(ans.keys())]
        
