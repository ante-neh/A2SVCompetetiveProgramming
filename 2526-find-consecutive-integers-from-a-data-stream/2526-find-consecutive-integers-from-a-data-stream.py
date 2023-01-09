class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.counter = k
        self.dataStream = 0
    def consec(self, num: int) -> bool:
        if num == self.val:
            self.dataStream += 1
        else:
            self.dataStream = 0
            
        if self.dataStream == self.counter:
            self.dataStream -= 1
            return True
        else:
            return False
        
        
        
            

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)