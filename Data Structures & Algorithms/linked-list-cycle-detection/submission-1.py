# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head.next
        while p1 != p2:
            p1 = p1.next
            if p1 == None:
                return False
            p2 = p2.next
            if p2 == None:
                return False
            p2 = p2.next
            if p2 == None:
                return False
        return True