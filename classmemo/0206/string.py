for t in range(10):
    case = int(input())
    word = input()
    board = input()
    N,M = len(board), len(word)
    cnt = 0
    for s in range(N-M+1):
        pattern = True
        for i in range(M):
            if word[i]!=board[s+i]:
                pattern = False
                break
        if pattern:
            cnt+=1
    print(f'#{case} {cnt}')