def is_palin(thing):
    for n in range(len(thing)//2):
        if thing[n]!=thing[-n-1]:
            result = False
            break
        else:
            result = True
    return result

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    frame = [list(input()) for _ in range(N)]
    result = None
    for i in range(N):
        for j in range(N-M+1):
            word = ''
            for n in range(M):
                word+=frame[i][j+n]
            if is_palin(word):
                result = word
                break
    if result == None:
        for j in range(N):
            for i in range(N-M+1):
                word = ''
                for n in range(M):
                    word+=frame[i+n][j]
                if is_palin(word):
                    result = word
                    break
    print(f'#{t+1} {result}')