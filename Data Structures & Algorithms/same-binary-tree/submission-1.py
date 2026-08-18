# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        res = True
        def dfs(node1, node2):
            nonlocal res
            if not res:
                return False
            if not node1 and not node2:
                return
            if not node1 or not node2 or node1.val != node2.val:
                res = False
                return
            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)
        dfs(p, q)
        return res