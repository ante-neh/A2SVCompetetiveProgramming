class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        temp = self.head
        while temp and index > 0:
            temp = temp.next
            index -= 1

        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            newNode = ListNode(val)
            self.head = newNode
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next

            temp.next = ListNode(val)
            
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 

        elif index == 0:
            self.addAtHead(val)

        elif index == self.length:
            self.addAtTail(val)

        else:
            temp = self.head
            index -= 1

            while index:
                temp = temp.next
                index -= 1

            newNode = ListNode(val)
            temp.next, newNode.next = newNode, temp.next

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return 

        elif index == 0:
            self.head = self.head.next

        else:
            temp = self.head
            index = index - 1

            while index:
                temp = temp.next
                index -= 1

            temp.next = temp.next.next

        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)