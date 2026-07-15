# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        bef = None
        while second:
            nxt = second.next
            second.next = bef
            bef = second
            second = nxt

        end = bef
        beg = head
        while end:
            nxt = beg.next
            beg.next = end
            enxt = end.next
            end.next = nxt
            beg = nxt
            end = enxt
    


