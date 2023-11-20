class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        nums = set(nums)
        
        def backtrack(cur):
            if len(cur) == length:
                if cur not in nums:
                    return cur

                return ""

            addZero = backtrack(cur + "0")
            if addZero:
                return addZero

            return backtrack(cur + "1")

        return backtrack("")