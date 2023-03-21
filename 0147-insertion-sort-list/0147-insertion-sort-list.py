# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        dummy = ListNode()
        cur = dummy
        
        while head:
            nums.append(head.val)
            head = head.next
            
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
                
            nums[j + 1] = key
            
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
            
        return dummy.next