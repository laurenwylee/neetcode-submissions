# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        k = length - n
        curr = head
        bef = None
        while curr and k > 0:
            k -= 1
            bef = curr
            curr = curr.next
        if bef == None:
            return curr.next
        bef.next = curr.next
        return head
