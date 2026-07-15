# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(nd):
            if nd == None: 
                return 0
            return 1 + max(get_height(nd.left), get_height(nd.right))
        if root == None:
            return True
        else:
            if abs(get_height(root.left) - get_height(root.right)) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False