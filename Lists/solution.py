if __name__ == '__main__':
    N = int(input())
    res = []
    
    for i in range(N):
        inp= input().split()
        
        if inp[0] == 'print':
            print(res)
        elif inp[0] == 'insert':
            res.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == 'remove':
            res.remove(int(inp[1]))
        elif inp[0] == 'append':
            res.append(int(inp[1]))
        elif inp[0] == 'pop':
            res.pop()
        elif inp[0] == 'reverse':
            res.reverse()
        else:
            res.sort()
            