# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxHeight(root):
            if not root:
                return 0
            return 1 + max(maxHeight(root.left), maxHeight(root.right))
        stack = [root]
        m = 0
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            m = max(m, maxHeight(node.left) + maxHeight(node.right))
        return m