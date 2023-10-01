class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderCount = defaultdict(lambda:float('inf'))

        for index, c in enumerate(order):
            orderCount[c] = index

        s = sorted(s, key=lambda c:(orderCount[c]))

        return ''.join(s)