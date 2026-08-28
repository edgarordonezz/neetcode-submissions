# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # for every node on the left subtree
        # low = curr.left, high = curr.val
        # as long as low <= curr.val <= parent
        # so at our root, low, high = -inf, inf
        low = float("-inf")
        high = float("inf")
        def dfs(root, low, high):
            if root is None:
                return True
            x = root
            if not (low < x.val < high):
                return False
            left_ = dfs(x.left, low, x.val) # going left, x.left <= x
            right_ = dfs(x.right, x.val, high) # going right, x <= x.right
            return left_ and right_
        
        return dfs(root, low, high)