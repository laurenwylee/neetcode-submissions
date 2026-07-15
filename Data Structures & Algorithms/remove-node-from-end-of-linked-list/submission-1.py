# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = head
        ct = 0
        while ct != n:
            r = r.next
            ct += 1
        while r != None:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next

