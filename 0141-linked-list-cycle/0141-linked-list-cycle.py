# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# approach 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = set()
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
    
# approach 2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False