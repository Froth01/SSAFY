def check(lst):
    for j in range(W):
        point = lst[0][j]
        cnt = 1
        for i in range(1,D):
            if cnt+(D-i) < K or cnt >= K:
                break
            elif lst[i][j] == point:
                cnt += 1
            else:
                point = lst[i][j]
                cnt = 1
        if cnt < K:
            return False
    return True

def testing(lst,limit,lvl):
    global answer
    if answer:
        return
    elif lvl == limit:
        if check(lst):
            answer = limit
        return
    for d in range(lvl,D):
        for type in inject:
            line = [type]*W
            lst_in = lst[:]
            lst_in[d] = line
            testing(lst_in,limit,lvl+1)
            if answer:
                return


T = int(input())
for t in range(T):
    D,W,K = map(int,input().split())
    frame = [list(map(int,input().split())) for _ in range(D)]
    inject = [0,1]
    if check(frame):
        print(f'#{t+1} {0}')
        continue
    answer = 0
    for level in range(1,K):
        testing(frame,level,0)
        if answer :
            break
    if not answer:
        print(f'#{t+1} {K}')
    else:
        print(f'#{t+1} {answer}')


