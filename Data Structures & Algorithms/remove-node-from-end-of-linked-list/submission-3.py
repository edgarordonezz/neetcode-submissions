# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        # we want slow to be before fast where fast has advanced n steps already
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            # increment both until fast.next is None
            slow = slow.next
            fast = fast.next
        # once that happens, slow will point to the node before the one we want removed
        slow.next = slow.next.next
        return dummy.next