class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        i = 1

        while i * 2 <= n:
            if not n % i:
                count += 1

            i += 1
        

        return count + 1 == 3