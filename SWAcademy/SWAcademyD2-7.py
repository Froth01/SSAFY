#1285.아름이의 돌 던지기 파이썬은 제출못함

T = int(input())
for t in range(T):
    N = int(input())
    tie = []
    throw = list(map(int,input().split()))
    for n in range(N):
        throw[n]=abs(throw[n])
    for a in range(N):
        if throw[a]==min(throw):
            tie.append(throw[a])
    first = min(throw)
    print(f'#{t+1} {first} {len(tie)}')
    