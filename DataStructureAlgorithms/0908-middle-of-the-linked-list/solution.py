# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pA = head
        pB = head
        while pA and pA.next:
            pA = pA.next.next
            pB = pB.next
        return pB
        
