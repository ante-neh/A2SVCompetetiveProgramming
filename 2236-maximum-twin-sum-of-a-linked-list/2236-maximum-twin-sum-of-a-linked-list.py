# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        nums = []

        while temp:
            nums.append(temp.val)
            temp = temp.next
        n = len(nums)
        maxTwinSum = 0

        for i in range(n // 2):
            maxTwinSum = max(nums[i] + nums[n - i - 1], maxTwinSum)

        return maxTwinSum