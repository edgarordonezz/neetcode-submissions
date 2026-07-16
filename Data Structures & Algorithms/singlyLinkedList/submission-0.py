class ListNode:
    def __init__ (self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            else:
                cur = cur.next
                i += 1
        return -1
        

    def insertHead(self, val: int) -> None:
        curr = ListNode(val) # Initialize curr with val

        curr.next = self.head # Copy where self.head currently points, and store that in curr.next 
                              # so the new node knows what used first

        self.head = curr # New node is now the head
        if self.tail is None: # if the list was empty, make the current node head & tail
            self.tail = curr

    def insertTail(self, val: int) -> None:

        curr = ListNode(val) # Initialize node
        if self.head is None: # Empty case
            self.head = curr
            self.tail = curr
            return # return so next lines dont execute
        self.tail.next = curr
        self.tail = curr
        
        

    def remove(self, index: int) -> bool:

        if self.head is None:
            return False
        
        if index == 0: # if index is at head
            self.head = self.head.next # make head point to next node
            if self.head is None: # if self.head is empty
                self.tail = None # tail should also be empty
            return True

        prev = None
        curr = self.head
        i = 0
        while curr:
            if i == index:
                prev.next = curr.next 
                if curr == self.tail:
                    self.tail = prev
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

        
