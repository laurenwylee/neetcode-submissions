# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {}
        pre_i = 0
        for i, v in enumerate(inorder):
            idx_map[v] = i
        def build(l, r):
            nonlocal pre_i
            if l > r:
                return None
            root = TreeNode(preorder[pre_i])
            pre_i += 1
            mid = idx_map[root.val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(inorder) - 1)

