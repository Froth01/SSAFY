def make(make_sec,make_ea,mans):
    man_cnt = 0
    for m in mans:
        left = (m//make_sec)*make_ea-man_cnt
        if left<=0:
            return 'Impossible'
        else:
            man_cnt+=1
    return 'Possible'

T = int(input())
for t in range(T):
    N,M,K = map(int,input().split())
    man = list(map(int,input().split()))
    man.sort()
    print(f'#{t+1} {make(M,K,man)}')