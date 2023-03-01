class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        def helper(l, r):
            if l > r:
                return 1
            else:
                s[l], s[r] = s[r], s[l]
                return helper(l + 1, r - 1)
        
        return helper(l, r)