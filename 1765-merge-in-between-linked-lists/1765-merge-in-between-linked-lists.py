# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left, right = list1, list1
        temp = list1

        while temp and a > 0:
            left = temp
            temp = temp.next
            a -= 1

        temp = list1

        while temp and b > -1:
            right = temp
            temp = temp.next
            b -= 1
        

        right = right.next
        temp = list2

        while temp.next:
            temp = temp.next

        left.next = list2
        temp.next = right

        return list1