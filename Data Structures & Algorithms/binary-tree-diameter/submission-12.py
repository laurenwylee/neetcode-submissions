# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLongest(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.getLongest(root.left), self.getLongest(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        mid = self.getLongest(root.left) + self.getLongest(root.right)
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        return max(mid, left, right)

        