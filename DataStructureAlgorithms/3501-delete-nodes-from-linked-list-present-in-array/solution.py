# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        top=ListNode(0,head)
        curr=head
        prev=top
        num_set=set(nums)
        while curr:
            if curr.val in num_set:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return top.next
            
        
