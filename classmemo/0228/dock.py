T = int(input())
for t in range(T):
    N = int(input())
    dock_lst = []
    for n in range(N):
        start,end = map(int,input().split())
        dock_lst.append((end,start))
    dock_lst.sort()
    cnt = 1
    first = dock_lst.pop(0)
    for dock in dock_lst:
        if dock[1]>=first[0]:
            cnt+=1
            first = dock
    print(f'#{t+1} {cnt}')