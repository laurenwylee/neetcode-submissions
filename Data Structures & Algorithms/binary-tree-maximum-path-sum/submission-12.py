# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -math.inf
        def dfs(nd):
            nonlocal result
            if nd == None:
                return 0
            left = max(0, dfs(nd.left))
            right = max(0, dfs(nd.right))
            result = max(result, nd.val + left + right)
            return nd.val + max(left, right)
        dfs(root)
        return result
            