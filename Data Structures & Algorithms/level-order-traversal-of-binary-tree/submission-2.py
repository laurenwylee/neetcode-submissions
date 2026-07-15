# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        if root:
            queue.append(root)
        ret = []
        while queue:
            lvl = []
            for _ in range(len(queue)):
                nd = queue.popleft()
                lvl.append(nd.val)
                if nd.left:
                    queue.append(nd.left)
                if nd.right:
                    queue.append(nd.right)
            ret.append(lvl)
        return ret
        

