# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        # map node indices using a map
        for i, val in enumerate(inorder):
            indices[val] = i
        self.preidx = 0
        def dfs(l, r):
            if l > r:
                return None
            rval = preorder[self.preidx]
            self.preidx += 1
            root = TreeNode(rval)
            mid = indices[rval]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
            
        return dfs(0, len(inorder) - 1)