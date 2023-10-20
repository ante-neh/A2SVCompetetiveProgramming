class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        self.head.next = Node(url, self.head)
        self.head = self.head.next

    def back(self, steps: int) -> str:
        while self.head.prev and steps > 0:
            self.head = self.head.prev
            steps -= 1

        return self.head.val

    def forward(self, steps: int) -> str:
        while self.head.next and steps > 0:
            self.head = self.head.next
            steps -= 1

        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)