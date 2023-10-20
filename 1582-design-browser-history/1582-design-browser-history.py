class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.cur = self.head
        self.curLength = 1
        self.length = 1

    def visit(self, url: str) -> None:
        self.cur.next = Node(url)
        self.cur = self.cur.next
        self.curLength += 1
        self.length = self.curLength

    def back(self, steps: int) -> str:
        if self.curLength - steps < 0:
            self.cur = self.head
            self.curLength = 0
            return self.cur.val
        
        else:
            slow, fast = self.head, self.head
            while fast and steps > 0:
                fast = fast.next
                steps -= 1
                self.curLength -= 1
            
            while fast and fast.val != self.cur.val:
                slow = slow.next
                fast = fast.next

            self.cur = slow

            return self.cur.val

    def forward(self, steps: int) -> str:
        temp = self.cur
        self.curLength = min(self.curLength + steps, self.length)

        while temp.next and steps > 0:
            temp = temp.next
            steps -= 1

        self.cur = temp

        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)