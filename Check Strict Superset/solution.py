# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())

for i in range(n):
    B = set(map(int, input().split()))
    if len(B.difference(A)):
        res = False
        break
    else:
        res = True
print(res)