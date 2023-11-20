class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        nums = set(nums)
        
        def backtrack(cur):
            if len(cur) == length:
                res = "".join(cur)
                if res not in nums:
                    return res 
                return ""


            for c in ['0', '1']:
                cur.append(c)
                res = backtrack(cur)
                if res:
                    return res

                cur.pop()
        
        return backtrack([])