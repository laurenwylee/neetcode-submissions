# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []
        if not root:
            return "NULL"
        q = deque([root])
        while q:
            nd = q.popleft()
            if not nd:
                ret.append("NULL")
            else:
                ret.append(str(nd.val))
                q.append(nd.left)
                q.append(nd.right)
        print(ret)
        return ",".join(ret)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inp = data.split(",")
        root = TreeNode()
        if inp[0] == "NULL":
            return None
        root = TreeNode(int(inp[0]))
        q = deque([root])
        i = 1
        while q:
            nd = q.popleft()
            if inp[i] != "NULL":
                nd.left = TreeNode(int(inp[i]))
                q.append(nd.left)
            i += 1
            if inp[i] != "NULL":
                nd.right = TreeNode(int(inp[i]))
                q.append(nd.right)
            i += 1
        return root

