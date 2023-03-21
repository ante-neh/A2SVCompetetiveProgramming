t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    write = 0
    maxSum = 0

    for read in range(len(nums)):
        if nums[read] * nums[write] < 0:
            maxSum += nums[write]
            write = read
        
        else:
            if nums[read] > nums[write]:
                write= read
    
    maxSum += nums[write]

    print(maxSum)
