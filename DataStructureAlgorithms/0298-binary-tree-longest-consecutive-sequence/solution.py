# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxlen=1
        def dfs(currnode):
            if not currnode:
                return 0
            if (not currnode.left) and (not currnode.right):
                return 1
            a=b=0
            ans=1
            a = dfs(currnode.left)
            b = dfs(currnode.right)
            if (currnode.left and currnode.left.val-currnode.val==1):
                self.maxlen=max(self.maxlen,1+a)
                ans=1+a
            if (currnode.right) and (currnode.right.val-currnode.val==1):
                self.maxlen=max(self.maxlen,1+b)
                ans=max(ans,1+b)
            return ans
        dfs(root)
        return self.maxlen
        
                


        
