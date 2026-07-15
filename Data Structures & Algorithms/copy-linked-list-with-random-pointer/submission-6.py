"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d = {}
        curr = head
        curr_copy = Node(0)
        while curr:
            if curr not in d:
                d[curr] = Node(curr.val)
            curr_copy.next = d[curr]
            curr_copy = curr_copy.next
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = Node(curr.random.val)
                curr_copy.random = d[curr.random]
            curr = curr.next
            
        return d[head]