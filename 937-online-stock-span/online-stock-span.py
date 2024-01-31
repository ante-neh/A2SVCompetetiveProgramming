class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 0
        while self.stack and self.stack[-1][0] <= price:
            val, count = self.stack.pop()
            span += count

        self.stack.append([price, span + 1])

        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)