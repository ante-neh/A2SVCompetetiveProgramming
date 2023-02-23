n, s =map(int, input().split())
nums = list(map(int, input().split()))

left = 0
currSum = 0
maxLen = 0

for right in range(len(nums)):
    currSum += nums[right]
    while currSum > s:
        currSum -= nums[left]
        left += 1
    
    maxLen = max(maxLen, right - left + 1)

print(maxLen)

