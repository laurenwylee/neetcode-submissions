# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(list1, list2):
            curr1 = list1
            curr2 = list2
            dummy = node = ListNode()
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    node.next = curr1
                    curr1 = curr1.next
                    node = node.next
                else:
                    node.next = curr2
                    curr2 = curr2.next
                    node = node.next
            if curr1:
                node.next = curr1
            if curr2:
                node.next = curr2
            return dummy.next
        if lists:
            before = lists[0]
            for i in range(1, len(lists)):
                before = mergeTwo(before, lists[i])
            return before
        return None