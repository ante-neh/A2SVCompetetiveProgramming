# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = []
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next


        numberOfNodes, mod = length //k, length % k
        temp = head

        for i in range(k):
            result.append(temp)
            for _ in range(numberOfNodes - 1 + (1 if mod else 0)):
                if not temp:
                    break

                temp = temp.next

            mod -= 1 if mod else 0
            if temp:
                temp.next, temp = None, temp.next
            
        return result








