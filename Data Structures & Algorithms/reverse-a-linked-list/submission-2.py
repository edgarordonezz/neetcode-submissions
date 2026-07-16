# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr: # while current node exists
            temp = curr.next # store next node
            curr.next = prev # set next node to prev
            prev = curr # set previous node to current node
            curr = temp # set current node to temp
        return prev # return previous tail                                              