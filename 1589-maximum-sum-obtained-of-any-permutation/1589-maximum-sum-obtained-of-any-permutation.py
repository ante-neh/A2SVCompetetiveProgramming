class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        overLap = [0] * (len(nums) + 1)
        maxSum = 0
        
        #forming the frequencies of requests array
        for request in requests:
            overLap[request[0]] += 1
            overLap[request[1] + 1] -= 1
            
        #forming the prefix sum of the requests array
        for i in range(1,len(overLap)):
            overLap[i] += overLap[i - 1]
            
        #sorting the requests array and the given array in reverse order
        nums.sort(reverse = True)
        overLap.sort(reverse = True)
        
        #calculating the maximum sum obtained of any permutation
        for i in range(len(nums)):
            maxSum += nums[i] * overLap[i]
            
        modulo = 10 ** 9 + 7
        
        return maxSum % modulo
            