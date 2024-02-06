def is_palin(thing):
    for n in range(len(thing)//2):
        if thing[n]!=thing[-n-1]:
            result = False
            break
        else:
            result = True
    return result

for t in range(10):
    N = int(input())
    frame = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(N):
        for j in range(9-N):
            word = ''
            for n in range(N):
                word += frame[i][j+n]
            if is_palin(word):
                cnt+=1
    for j in range(N):
        for i in range(9-N):
            word = ''
            for n in range(N):
                word += frame[i+n][j]
            if is_palin(word):
                cnt+=1
    print(f'#{t+1} {cnt}')