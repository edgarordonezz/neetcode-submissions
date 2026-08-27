# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Good Node: if path from root to x contains no nodes with a greater value than the value of x
        # we'll use dfs for this
        count = 0
        maxSoFar = root.val
        def dfs(root, maxSoFar):
            nonlocal count
            if root is None:
                return 0
            curr = root
            if curr.val >= maxSoFar:
                count += 1
            maxSoFar = max(curr.val, maxSoFar)
            left = dfs(curr.left, maxSoFar)
            right = dfs(curr.right, maxSoFar)
        dfs(root, maxSoFar)
        return count