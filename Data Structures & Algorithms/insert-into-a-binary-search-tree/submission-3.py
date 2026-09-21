# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def traverse(node):
            if node.val > val:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = TreeNode(val)
        traverse(root)
        return root
