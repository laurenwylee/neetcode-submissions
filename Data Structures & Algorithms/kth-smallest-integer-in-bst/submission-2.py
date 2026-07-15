# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]
        count = 0
        while stack:
            nd, processed = stack.pop()
            if processed:
                count += 1
                if count == k:
                    return nd.val
            else:
                if nd.right:
                    stack.append((nd.right, False))
                stack.append((nd, True))
                if nd.left:
                    stack.append((nd.left, False))
        print("none")
        return count