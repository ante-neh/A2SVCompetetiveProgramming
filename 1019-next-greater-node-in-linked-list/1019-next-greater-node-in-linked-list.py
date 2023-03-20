# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        nums = []
        
        while temp:
            nums.append(temp.val)
            temp = temp.next
        nextGreater = [0] * len(nums)    
        stack = []
        
        for index, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                val, i = stack.pop()
                nextGreater[i] = num
                
            stack.append([num, index])
            
        return nextGreater
                
            
        