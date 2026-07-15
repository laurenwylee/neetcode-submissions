# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr != None:
            curr = curr.next
            counter += 1
        curr = head
        x = (counter - n) + 1
        if x == 1:
            return curr.next
        while x > 2:
            curr = curr.next
            x -= 1
        curr.next = curr.next.next
        return head
        