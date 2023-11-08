class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.maxFreq = 0
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxFreq = max(self.maxFreq, self.freq[val])
        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.stacks[self.maxFreq]:
            self.maxFreq -= 1

        return val


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()