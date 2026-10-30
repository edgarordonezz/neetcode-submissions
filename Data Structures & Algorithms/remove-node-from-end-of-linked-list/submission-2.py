# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        # get length of LL
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        # length - n is the node we want removed
        m = length - n - 1
        new = None
        curr = head
        if m < 0:
            new = curr.next
            return new
        # iterate right before m
        for _ in range(m):
            curr = curr.next
        # unlinked it
        curr.next = curr.next.next
        return head



        


        