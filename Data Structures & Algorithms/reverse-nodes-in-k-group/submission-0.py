# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Brute force
        arr = []
        current = head

        # dump list elements into array
        while current:
            arr.append(current.val)
            current = current.next

        n = len(arr)
        for i in range(n // k):
            start = i * k
            end = start + (k-1)
            arr[start:end+1:] = arr[start:end+1:][::-1]

        dummy = ListNode(0, None)
        mover = dummy
        for i in range(len(arr)):
            mover.next = ListNode(arr[i])
            mover = mover.next
        
        return dummy.next