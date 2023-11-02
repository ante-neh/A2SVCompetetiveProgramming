class ListNode:
    def __init__(self, val = 0,  next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode()
        self.head.next = self.head
        self.capacity = k
        self.length = 0
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            node = ListNode(value, self.tail.next)
            self.tail.next = node
            self.tail = node
            self.length += 1
            return True

        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head.next = self.head.next.next
            self.length -= 1
            
            if self.length == 0:
                self.tail = self.head

            return True

        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.next.val
        
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        
        return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()