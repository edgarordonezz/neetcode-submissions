# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None: # while fast and fast.next still point to something
            fast = fast.next.next # fast pointer
            slow = slow.next # slow pointer
            if slow == fast: # if slow and fast ever point to the same node
                return True # we have a cycle
        return False # if fast finished, we have no cycle