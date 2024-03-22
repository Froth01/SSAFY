def pullout(heightsum,x):
    if heightsum >= B:
        result.append(heightsum-B)
        return
    for h in range(x,len(worker)):
        if heightsum+worker[h] < B:
            pullout(heightsum+worker[h],h+1)
        else:
            result.append((heightsum+worker[h])-B)



T = int(input())
for t in range(T):
    N,B = map(int,input().split())
    worker = list(map(int,input().split()))
    result = []
    for w in range(N):
        pullout(worker[w],w+1)
    print(f'#{t+1} {min(result)}')