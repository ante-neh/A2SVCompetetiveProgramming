n = int(input())
englishSub = set(map(int, input().split()))
m = int(input())
frenchSub = set(map(int, input().split()))

difference = englishSub.difference(frenchSub)

print(len(difference))