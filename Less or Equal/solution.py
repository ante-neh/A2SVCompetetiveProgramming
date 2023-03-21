n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
x = -1
for r in range(len(nums)):
    if r + 1 == k:
        if r + 1 < len(nums) and nums[r + 1] != nums[r]:
            x = nums[r]
        break

if k == 0:
    if nums[0] <= 1:
        print(-1)

    else:
        print(1)

elif n == k:
    print(nums[-1])

else:
    print(x)