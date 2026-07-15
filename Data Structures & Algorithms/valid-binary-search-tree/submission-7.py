# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root,-1001, 1001)])
        while queue:
            length = len(queue)
            for _ in range(length):
                nd, l, r = queue.popleft()
                if nd.val <= l or nd.val >= r:
                    return False
                if nd.left:
                    queue.append((nd.left,l, nd.val))
                if nd.right:
                    queue.append((nd.right, nd.val, r))
        return True