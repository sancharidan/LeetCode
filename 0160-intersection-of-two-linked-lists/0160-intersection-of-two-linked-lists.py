# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
# Method 1 - O(n) auxillary space
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
#         l1=headA
#         l2=headB
#         visited = set()
#         while l1:
#             visited.add(l1)
#             l1=l1.next
            
#         while l2:
#             if l2 in visited:
#                 return l2
#             l2=l2.next
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        l1=headA
        l2=headB
        len1=0
        len2=0
        while l1:
            len1 = len1 + 1
            l1 = l1.next
        
        while l2:
            len2 = len2 + 1
            l2 = l2.next
        
        node1=headA
        node2=headB
        if len2>len1:
            tmp = node1
            node1=node2
            node2=tmp
                
        abs_diff = abs(len1-len2)
        cnt = 0 
        while cnt<abs_diff:
            node1=node1.next
            cnt=cnt+1

        while node1 and node2:
            if node1==node2:
                return node1
            node1 = node1.next
            node2 = node2.next

                    