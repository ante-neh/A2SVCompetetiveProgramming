class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strint(num1)*self.strint(num2))
    def strint(self,n):
        result=0
        for i in range(len(n)):
            result = result*10 + ord(n[i])-ord('0')
        return result