T = int(input())
for t in range(T):
    N = int(input())
    bus = []
    stop = []
    for n in range(N):
        bus.append(list(map(int,input().split())))
    P = int(input())
    result = [0]*P
    for p in range(P):
        stop.append(int(input()))
    ############# 입력
    for b in range(len(bus)):
        for s in range(len(stop)):
            if bus[b][0]<=stop[s]<=bus[b][1]:
                result[s]+=1
    print(f'#{t+1}',end=' ')
    print(*result)




