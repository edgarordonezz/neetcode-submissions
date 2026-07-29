class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        new_head = None
        last_tail = None
        
        while head:
        # first check if group has enough nodes
            check = head
            for i in range(k):
                if check is None:
                    if last_tail: last_tail.next = head
                    return new_head if new_head else head
                check = check.next

            prev = None
            heads = head
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if new_head is None:
                new_head = prev
            
            if last_tail:
                last_tail.next = prev
            
            last_tail = heads
            head = curr
            heads.next = curr

        return new_head