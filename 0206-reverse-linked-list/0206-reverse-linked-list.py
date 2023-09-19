# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        prev = head
        curr = head
        
        while prev and curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head.next = None
        head = prev
        return head