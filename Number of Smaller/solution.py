n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
numOfSmaller = []

p1, p2 = 0, 0

while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] < nums2[p2]:
        p1 += 1
    
    else:
        numOfSmaller.append(p1)
        p2 += 1

while p2 < len(nums2):
    numOfSmaller.append(p1)
    p2 += 1

print(*numOfSmaller)