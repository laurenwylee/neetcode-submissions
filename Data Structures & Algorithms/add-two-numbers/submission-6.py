# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = 0
            if s > 9:
                carry = s // 10
                s = s % 10
            print("l1 and l2")
            print(s)
            head.next = ListNode(s)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + carry
            carry = 0
            if s > 9:
                carry = s // 10
                s = s % 10
            print("l1")
            print(s)
            head.next = ListNode(s)
            head = head.next
            l1 = l1.next
        while l2:
            s = l2.val + carry
            carry = 0
            if s > 9:
                carry = s // 10
                s = s % 10
            print("l2")
            print(s)
            head.next = ListNode(s)
            head = head.next
            l2 = l2.next
        # return head
        if carry != 0:
            head.next = ListNode(carry)
            
        return dummy.next
        
