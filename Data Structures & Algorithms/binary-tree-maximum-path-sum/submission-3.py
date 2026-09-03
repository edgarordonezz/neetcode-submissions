# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # brute force we would try each node at every path
        # 10 - 15 + 20 = 15
        # -15 + 20 + 5 = 10
        # 20 + 5 = 25
        # -5 + 15 + 20 + 5 = 35
        # 15 + 20 + 5 = 40
        max_path = float("-inf")
        def dfs(node):
            nonlocal max_path
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            # compare max_paths, 0 is set in case there is a negative number, we'll choose 0 as the greatest path
            max_path = max(max_path, (node.val + max(0, l) + max(0, r)))
            # return the node's value + its greater child
            return node.val + max(0, l, r)
        dfs(root)
        return max_path