class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)

        return reverse(0, len(s) - 1)