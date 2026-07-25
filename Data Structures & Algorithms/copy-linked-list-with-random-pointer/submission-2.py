"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        hashy = {}
        old_node = head

        while old_node:
            new_node = Node(old_node.val)
            hashy[old_node] = new_node
            old_node = old_node.next
        # reset to iterate again
        old_node = head

        while old_node:
            
            hashy[old_node].next = hashy.get(old_node.next)
            hashy[old_node].random = hashy.get(old_node.random)
            old_node = old_node.next

        return hashy.get(head)