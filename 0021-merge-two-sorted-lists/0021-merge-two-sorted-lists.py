# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         if not list1:
#             return list2
#         if not list2:
#             return list1
        
#         ptr1 = list1
#         ptr2 = list2
#         while ptr1 and ptr2:
#             if ptr1.val<=ptr2.val:
#                 tmp = ptr1.next
#                 ptr1.next = ptr2
#                 if not tmp:
#                     return list1
#                 else:
#                     ptr1 = tmp
#             elif ptr1.val > ptr2.val:
#                 tmp = ptr2.next
#                 ptr2.next = ptr1
#                 if not tmp:
#                     return list2
#                 else:
#                     ptr2 = tmp

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
                
        
        