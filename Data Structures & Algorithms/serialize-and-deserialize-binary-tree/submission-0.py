from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if node is None:
                res.append("N")
                return
            # node -> left -> right: preorder traversal, good stuff
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue = deque(data.split(","))
        def dfs():
            val = queue.popleft()
            if val == "N":
                return None
            else:
                val = int(val)
            node = TreeNode(val)
            l, r = dfs(), dfs()
            node.left, node.right = l, r
            return node
        return dfs()