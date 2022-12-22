class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, i = 0, 0
        binarySum = []
        a, b = a[::-1], b[::-1]
        
        while i < len(a) or i < len(b):
            temp = carry + (int(a[i]) if i < len(a) else 0) + (int(b[i]) if i < len(b) else 0)
            binarySum.append(str(temp % 2))
            carry = temp // 2
            i += 1
            
        if carry:
            binarySum.append("1")
            
        return ''.join(binarySum[::-1])