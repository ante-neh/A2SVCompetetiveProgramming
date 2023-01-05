class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        y = list(num2)
        a = int(num1[0])
        b = int(num1[1][:-1])
        c = int(num2[0])
        d = int(num2[1][:-1])
        
        
        return str((a * c) - (b * d)) + "+" + str((b * c) + (a * d)) +"i"