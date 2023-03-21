# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        dummy = ListNode()
        cur = dummy
        if not head:
            return None
        
        while head:
            nums.append(head.val)
            head = head.next
            
        nums = nums[::-1]
        k = k % len(nums)
        l, r = 0, k - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        l, r = k, len(nums) - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
            
        return dummy.next