# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if root val is greater than p and greater than q, go left
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # if root val is greater than p and greater than q, go right
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # if left<=root<=right OR left>=root>=right we found the LCA
        if root.val >= p.val and root.val <= q.val or root.val <= p.val and root.val >= q.val:
            return root