# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        curr = root
        # dfs, traverse down left and count, then right and count
        left = self.maxDepth(curr.left)
        right = self.maxDepth(curr.right)
        return max(left, right) + 1