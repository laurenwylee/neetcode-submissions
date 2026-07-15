# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = []
        stack = [(root, -101)]
        while stack:
            nd, maximum = stack.pop()
            if nd.val >= maximum:
                ret.append(nd.val)
            new_max = max(maximum, nd.val)
            if nd.left:
                stack.append((nd.left, new_max))
            if nd.right:
                stack.append((nd.right, new_max))
        return len(ret)
            

