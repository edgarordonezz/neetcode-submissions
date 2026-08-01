# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 -> 4
        # has to be 
        # 0 <- 1 <- 2 <- 3 <- 4
        current = head
        prev = None
        # while a node exists
        # store that value
        while current:
            # store the node.next value
            nxt = current.next
            current.next = prev
            # store current value
            temp = current
            # set prev to current value
            prev = temp 
            # advance
            current = nxt
        return prev