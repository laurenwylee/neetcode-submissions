# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the middle element
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        before = None
        while mid != None:
            nxt = mid.next
            mid.next = before
            before = mid
            mid = nxt
        # before points to the end of the list
        curr = head
        end = before
        while curr and end:
            nxt = curr.next
            end_nxt = end.next
            curr.next = end
            end.next = nxt
            curr = nxt
            end = end_nxt
        


