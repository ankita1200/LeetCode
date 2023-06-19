# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def traverse(node):
            if not node:
                return 0
            pos = 1 +traverse(node.next)
            if pos == n+1:
                node.next = node.next.next
            return pos
        
        temp = head
        l = 0
        while temp != None:
            l +=1
            temp = temp.next
        
        if n == l:
            return head.next
        
        curr = head
        traverse(curr)
        return head
        
