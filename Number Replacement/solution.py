def checker(number, string):
    d = {}
    
    for i in range(len(number)):
        if number[i] in d and d[number[i]] != string[i]:
            return False
            
        d[number[i]] = string[i]
        
    return True
    
n = int(input())
 
for i in range(n):
    length = int(input())
    number = list(map(int, input().split()))
    string = input()
    if checker(number, string):
        print("YES")
    else:
        print("NO")