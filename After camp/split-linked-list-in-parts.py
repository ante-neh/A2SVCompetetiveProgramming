# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        parts = length // k
        remainder = length % k

        cur = head
        result = []

        while k > 0:
            temp = cur
            result.append(cur)
            for i in range(parts + 1 - 1 if remainder > 0 else parts - 1):
                if not temp:
                    break
                temp = temp.next

            remainder -= 1 if remainder > 0 else 0

            cur = temp.next if temp else None
            if temp:
                temp.next = None

            k -= 1


        return result
