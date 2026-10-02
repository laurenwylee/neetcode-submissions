# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        before = None
        curr = head
        while curr:
            if before and curr:
                nd_val = gcd(before.val, curr.val)
                node = ListNode(nd_val)
                before.next = node
                node.next = curr
            before = curr
            curr = curr.next
        return head