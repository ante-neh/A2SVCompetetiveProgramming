class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=set(nums)
        s=list()
        for i in range(len(nums)):
            if i+1 not in l:
                s.append(i+1)
        return s