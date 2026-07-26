# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node 
        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0 # val1 is the value of current node l1 if it exists, if exhausted  = 0
            val2 = l2.val if l2 else 0 # val2 is the value of current node l2 if it exists, if exhausted  = 0

            total = val1 + val2 + carry
            new_digit = total % 10
            carry = total // 10

            current.next = ListNode(new_digit) # insert into node
            current = current.next

            if l1: # if l1 still has numbers, keep going
                l1 = l1.next
            if l2: # if l2 still has numbers, keep going
                l2 = l2.next
        
        return dummy.next