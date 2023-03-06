t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    c = min(a, b)
    d = (a + b) // 4

    print(min(c, d))
