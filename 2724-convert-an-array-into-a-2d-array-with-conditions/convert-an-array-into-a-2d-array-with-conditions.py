class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numsFreq = defaultdict(int)
        result = []
        
        for num in nums:
            i = numsFreq[num]
            if i == len(result):
                result.append([])

            result[i].append(num)
            numsFreq[num] += 1

        return result