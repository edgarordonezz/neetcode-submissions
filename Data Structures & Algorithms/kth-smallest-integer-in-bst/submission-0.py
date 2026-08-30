# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        node = 0
        def dfs(root):
            nonlocal count, node
            if root is None:
                return 0
            # dive down to the most left leaf
            dfs(root.left)
            count += 1
            if count == k:
                node = root.val
            dfs(root.right)
        dfs(root)
        return node