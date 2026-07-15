# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        curr2 = head
        while curr1 != None or curr2 != None:
            curr1 = curr1.next
            curr2 = curr2.next
            if curr2 == None:
                return False
            else:
                curr2 = curr2.next
            if curr2 and curr1:
                if curr1.val == curr2.val:
                    return True
            else:
                return False
        return False
