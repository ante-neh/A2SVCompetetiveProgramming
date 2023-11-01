class MyStack:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2.appendleft(x)

    def pop(self) -> int:
        self.stack1.pop()
        return self.stack2.popleft()
        
    def top(self) -> int:
        return self.stack2[0]

    def empty(self) -> bool:
        return len(self.stack2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()