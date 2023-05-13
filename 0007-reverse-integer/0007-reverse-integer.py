class Solution:
    def reverse(self, x: int) -> int:
        def convert(n):
            sum = 0
            while n > 0:
                rem = n % 10
                sum = sum * 10 + rem
                n //= 10
                
            return sum
        
        if x < 0:
            num = -1 * convert(abs(x))
        else:
            num = convert(abs(x))
        
        return num if -2 ** 31 <= num <= 2 **31 else 0