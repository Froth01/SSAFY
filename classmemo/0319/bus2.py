def bus(now,battery):
    global cnt, min_charge
    for n in range(1,battery+1):
        new = now + n
        if new >= N - 1:
            if min_charge > cnt:
                min_charge = cnt
            continue
        last = stop[new]
        cnt += 1
        if cnt>min_charge:
            cnt -= 1
            continue
        bus(new,last)
        cnt -= 1



T = int(input())
for t in range(T):
    N,*stop = map(int,input().split())
    min_charge = 99999
    cnt = 0
    bus(0,stop[0])
    print(f'#{t+1} {min_charge}')