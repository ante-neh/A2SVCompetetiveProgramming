t = int(input())
 
for i in range(t):
    n, c = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    numsCount = {}
     
    for num in nums:
        numsCount[num] = 1 + numsCount.get(num, 0)
        
    count = 0
     
    for orbit, freq in numsCount.items():
        if freq >= c:
            count += c
        else:
            count += freq
            
    print(count)