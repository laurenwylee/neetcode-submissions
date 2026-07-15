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
        if head:
            d = {}
            curr = head
            before = None
            while curr != None:
                nd = Node(curr.val)
                if before != None:
                    before.next = nd
                before = nd
                d[curr] = nd
                curr = curr.next
            curr = head
            while curr != None:
                nd = d[curr]
                if curr.random == None:
                    nd.random = None
                else:
                    rd = d[curr.random]
                    nd.random = rd
                curr = curr.next
            return d[head]
        else:
            return None