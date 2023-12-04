class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        count = 1
        while self.stock and self.stock[-1][0] <= price:
            p, c = self.stock.pop()
            count += c

        self.stock.append([price, count])

        return self.stock[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)