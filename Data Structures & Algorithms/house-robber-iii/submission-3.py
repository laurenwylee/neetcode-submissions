# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}
        def traverse(node):
            if node in cache:
                return cache[node]
            if node == None:
                return 0
        
            cache[node] = node.val
            if node.left:
                cache[node] += (traverse(node.left.right) + traverse(node.left.left))
            if node.right:
                cache[node] += (traverse(node.right.right) + traverse(node.right.left))
            cache[node] = max(cache[node], traverse(node.left) + traverse(node.right))
            return cache[node]
        return traverse(root)