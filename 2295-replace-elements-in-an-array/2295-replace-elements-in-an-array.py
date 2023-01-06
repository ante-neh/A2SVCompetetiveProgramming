class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numsToIndex = {}   
        
        for i in range(len(nums)):
            numsToIndex[nums[i]] = i  # put the index of the numbers to be replaced

        for operation in operations:
            index = numsToIndex[operation[0]]  # get the index of the number to be replaced
            nums[index] = operation[1]
            numsToIndex[operation[1]] = index  #put the index of the replaced value to the new value 
               
        return nums