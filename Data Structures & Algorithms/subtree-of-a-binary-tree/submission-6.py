# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == None and q == None:
                return True
            elif (p == None and q != None) or (p != None and q == None):
                return False
            else:
                if p.val == q.val:
                    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
                return False
        if subRoot == None:
            return True
        if root == None:
            return False
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
