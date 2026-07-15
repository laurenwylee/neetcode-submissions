# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        traversal = []
        while queue:
            target = len(queue)
            curr = []
            while target > 0:
                elem = queue.pop(0)
                curr.append(elem.val)
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
                target -= 1
            traversal.append(curr)
        return traversal
            


