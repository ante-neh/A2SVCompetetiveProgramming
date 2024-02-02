class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l, h = len(str(low)), len(str(high))
        sequentials = []
        nums = [str(i) for i in range(1, 10)]

        for k in range(l, h + 1):
            left = 0
            for right in range(len(nums)):
                if right - left + 1 == k:
                    num = int("".join(nums[left:right + 1]))
                    if low <= num <= high:
                        sequentials.append(num)

                    left += 1
                
        return sequentials
        
