class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLength = 0
        combinations = []

        def backtrack(index, cur):
            if index > len(arr):
                return

            combinations.append("".join(cur[:]))

            for i in range(index, len(arr)):
                backtrack(i + 1, cur + arr[i])
                    

        backtrack(0, "")
        
        for comb in combinations:
            if len(Counter(comb)) == len(comb):
                maxLength = max(maxLength, len(comb))
                
        return maxLength