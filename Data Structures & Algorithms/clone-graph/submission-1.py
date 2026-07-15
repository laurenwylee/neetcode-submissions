"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph = {}
        def dfs(node):
            if node.val in graph:
                new_node = graph[node.val]
            else:
                new_node = Node(val = node.val)
                graph[node.val] = new_node
                neighbors = []
                for u in node.neighbors:
                    neighbors.append(dfs(u))
                if neighbors:
                    new_node.neighbors = neighbors
            return new_node
        dfs(node)
        return graph[1]