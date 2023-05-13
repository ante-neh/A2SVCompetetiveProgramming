class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        def convert(n):
            num = []
            while n > 0:
                rem = n % 10
                num.append(str(rem))
                n //= 10
                
            return num
        
        nums = int("".join(convert(abs(x))))
        if x < 0:
            nums = -1 * nums
                   
        return nums if -2 ** 31 <= nums <= 2 ** 31 else 0