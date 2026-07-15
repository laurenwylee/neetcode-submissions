# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([])
        if root:
            queue.append(root)
        ret = []
        while queue:
            length = len(queue)
            for i in range(length):
                nd = queue.popleft()
                if i == length - 1:
                    ret.append(nd.val)
                if nd.left:
                    queue.append(nd.left)
                if nd.right:
                    queue.append(nd.right)
        return ret