class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                temp = carry + digits[i] + 1
            
            else:
                temp = carry + digits[i]
                
            if temp > 9:
                digits[i] = temp % 10
                
            else:
                digits[i] = temp
                
            carry = temp // 10
            
        if carry > 0 :
            digits.insert(0,carry)
            
        return digits