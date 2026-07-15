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
        cp = head
        d = {}
        while cp:
            d[cp] = Node(cp.val)
            cp = cp.next
        d[None] = None
        cp = head
        while cp:
            d[cp].next = d[cp.next]
            d[cp].random = d[cp.random]
            cp = cp.next
        return d[head]
    
