# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split in half
        # reverse smaller list
        # to split we use slow fast pointers until fast.next == None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # now reverse the second part
        # prev becomes the head of the reversed list
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # now combine them but stop at slow.next
        # firs = head, second = prev (reversed)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1

