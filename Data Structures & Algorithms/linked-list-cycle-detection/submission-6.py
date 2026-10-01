# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r = head
        t = head
        while t and r and r.next:
            r = r.next.next
            t = t.next
            if r == t:
                return True
        return False