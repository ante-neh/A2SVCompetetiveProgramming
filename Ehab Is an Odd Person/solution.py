n = int(input())
nums = list(map(int, input().split()))
flag1 = False
flag2 = False

for num in nums:
    if num % 2 == 0:
        flag1 = True
    
    else:
        flag2 = True

if flag1 and flag2:
    nums.sort()
    print(*nums)

else:
    print(*nums)