from collections import defaultdict
for _ in range(int(input())):
    row, col = list(map(int, input().split()))
    board = []
 
    for temp in range(row):
        l = list(map(int, input().split()))
        board.append(l)
 
 
    diagonal = defaultdict(int)
    diagonal2 = defaultdict(int)
    for i in range(len(board)):
        for j in range(len(board[i])):
            diagonal[j - i] += board[i][j]
            diagonal2[j + i] += board[i][j]
 
    maxSum = float('-inf')
 
    for i in range(len(board)):
        for j in range(len(board[i])):
            curSum = diagonal[j - i] + diagonal2[j + i] -board[i][j]
            maxSum =  max(maxSum, curSum)
 
 
    print(maxSum)