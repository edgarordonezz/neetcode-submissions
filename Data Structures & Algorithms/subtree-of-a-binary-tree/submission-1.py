# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):

            # if both are none return
            if not root and not subRoot:
                return True
            
            if not root or not subRoot or root.val != subRoot.val:
                return False

            if dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right):
                return True
            return False
        # find a matching starting point
        # if main tree is empty return false
        def find_match(root, subRoot):
            if root is None:
                return False
            if dfs(root, subRoot):
                return True
            return find_match(root.left, subRoot) or find_match(root.right, subRoot)

        return find_match(root, subRoot)