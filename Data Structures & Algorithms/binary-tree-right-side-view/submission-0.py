from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if root.left exists and root.right exists, only print root.right
        # have to go level by level
        # will be using BFS
        if root is None:
            return []
        res = []
        queue = deque([root])
        while len(queue) > 0:
        # while the queue has a node, check if it has
            level_size = len(queue) # number of nodes in current level
            for i in range(level_size):
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                if i == level_size - 1: 
                    res.append(curr.val)
        return res