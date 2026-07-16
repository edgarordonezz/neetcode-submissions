# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # use a dummy node because tail needs something to attach to first
        tail = dummy
        l1 = list1
        l2 = list2

        while l1 and l2:
            # if l1's value is less than or greater to l2's value
            # insert l1's value at tail.next
            # then set tail = tail.next
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            # else l2's value was less than so do the same but with l2's value
            else:
                tail.next = l2
                l2 = l2.next
            # increment tail
            tail = tail.next

        if l1: # if l1 still has nodes remaining, attach the rest of l1 (already sorted)
            tail.next = l1
        else: # otherwise l1 is emtpy, so attach the rest of l2 instead
            tail.next = l2
        
        return dummy.next
        

