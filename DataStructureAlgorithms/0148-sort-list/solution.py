# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    
    def merge(self,left,right):
        dummyHead = ListNode(0)
        tail = dummyHead
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummyHead.next
    
    def getMid(self,head):
        prevmid = None
        while head and head.next:
            prevmid = head if not prevmid else prevmid.next
            head = head.next.next
        mid = prevmid.next
        prevmid.next = None
        return mid


        
