from heapq import heapify, heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []
        counter = 0
        for l in lists:
            if l is None:
                continue
            else:
                heappush(heap, (l.val, counter, l))
                counter += 1

        while heap:
            value, count, node = heappop(heap) # get the value, count, and node of the root
            current.next = node
            current = current.next

            if node.next is None:
                continue
            else:
                heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next