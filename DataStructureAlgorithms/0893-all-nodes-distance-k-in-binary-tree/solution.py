# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        def dfs(node,parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root,None)
        que = deque([target])
        seen = {target}
        level=0
        while que and level < k:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        que.append(neighbor)
            level += 1
        return [node.val for node in que]
        

        
