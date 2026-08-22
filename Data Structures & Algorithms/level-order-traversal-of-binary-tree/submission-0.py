from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # we would do BFS here
        queue = deque([root])
        res = []
        # while the queue is not empty, process a full level
        while queue:
            # Get length of queue so we know how many nodes we have to collect
            n = len(queue)
            level = []
            while n > 0:
                # prioritize the element that got pushed in first
                curr = queue.popleft()
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                level.append(curr.val)
                n -= 1
            res.append(level)
        return res