# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # differ_count: |left - right| > 1
        # DFS and check heights
        res = True
        def dfs(root):
            nonlocal res
            if root is None:
                return 0 # height of empty tree is 0
            # get height of both trees
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if abs(left_depth - right_depth) > 1:
                res = False
            return 1 + max(left_depth, right_depth)
        dfs(root)
        return res

        