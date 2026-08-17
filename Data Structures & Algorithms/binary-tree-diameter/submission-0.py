# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def maxDepth(root):
            nonlocal res

            if root is None:
                return 0
            left_h = maxDepth(root.left)
            right_h = maxDepth(root.right)
            res = max(res, left_h + right_h)
            return 1 + max(left_h, right_h)
            
        maxDepth(root)
        return res