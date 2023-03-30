t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(3)

    else:
        y = ((n - 1) &n) ^ n
        print(y) if y^n != 0 else print(y+1)