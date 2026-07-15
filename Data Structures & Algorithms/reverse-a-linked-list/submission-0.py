# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        h = head
        n = head.next
        h.next = None
        while n != None:
            tmp = n
            n = n.next
            tmp.next = h
            h = tmp
        return h
            


