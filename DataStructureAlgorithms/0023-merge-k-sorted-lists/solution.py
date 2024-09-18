# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        curr = lists[0]
        for i in range(1,len(lists)):
            curr = self.merge(curr,lists[i])
        return curr
    
    def merge(self,left,right):
        dummyhead = ListNode(0)
        tail = dummyhead
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummyhead.next
    

        
