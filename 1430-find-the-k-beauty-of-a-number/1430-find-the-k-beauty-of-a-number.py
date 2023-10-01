class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        left = 0
        count = 0

        for right in range(len(num)):
            if right - left + 1 == k:
                if int(num[left:right + 1]) != 0 and int(num) % int(num[left:right + 1]) == 0:
                    count += 1

                left += 1

        return count