# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def countGoodNodes(r, m):
            if not r:
                return 0
            if r.val >= m:
                return 1 + countGoodNodes(r.left, max(r.val, m)) + countGoodNodes(r.right, max(r.val, m))
            else:
                 return countGoodNodes(r.left, max(r.val, m)) + countGoodNodes(r.right, max(r.val, m))
            
        return countGoodNodes(root, root.val)

                
