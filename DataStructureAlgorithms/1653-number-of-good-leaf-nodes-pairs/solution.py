# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def traverse_tree(curr_node,prev_node):
            if curr_node is None:
                return
            if curr_node.left is None and curr_node.right is None:
                leaf_nodes.add(curr_node)
            if prev_node is not None:
                graph[curr_node].append(prev_node)
                graph[prev_node].append(curr_node)
            traverse_tree(curr_node.left,curr_node)
            traverse_tree(curr_node.right,curr_node)
        
        ans=0
        leaf_nodes=set()
        graph=defaultdict(list)
        traverse_tree(root,None)
        for leaf in leaf_nodes:
            seen=set()
            queue=deque([(leaf,0)])
            seen.add(leaf)
            while queue:
                nodes_level=len(queue)
                for it in range(nodes_level):
                    currnode,dist=queue.popleft()
                    if (currnode in leaf_nodes) and (currnode is not leaf) and (dist<=distance):
                        ans+=1
                    for neighbor in graph[currnode]:
                        if neighbor not in seen:
                            queue.append((neighbor,dist+1))
                            seen.add(neighbor)
        return ans//2
                    



        
