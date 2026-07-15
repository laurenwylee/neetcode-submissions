# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        before = None
        head = ListNode()
        curr = head
        carry = 0
        while curr1 and curr2:
            summed = curr1.val + curr2.val + carry
            curr.val = summed % 10
            carry = summed // 10
            if before != None:
                before.next = curr
            before = curr
            curr = ListNode()
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            summed = curr1.val + carry
            curr.val = summed % 10
            carry = summed // 10
            if before != None:
                before.next = curr
            before = curr
            curr = ListNode()
            curr1 = curr1.next
        while curr2:
            summed = curr2.val + carry
            curr.val = summed % 10
            carry = summed // 10
            if before != None:
                before.next = curr
            before = curr
            curr = ListNode()
            curr2 = curr2.next
        if carry > 0:
            before.next = curr
            curr.val = carry
            # if curr1:
            #     curr.val += curr1.val
            # if curr2:
            #     curr.val += curr2.val
        return head
        
