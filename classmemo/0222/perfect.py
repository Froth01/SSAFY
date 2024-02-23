T = int(input())
for t in range(T):
    N = int(input())
    card = list(input().split())
    up = card[:N//2]
    down = card[N//2:]
    if N%2!=0:
        up = card[:N//2+1]
        down = card[N//2+1:]
    new = []
    for n in range(N//2):
        new.append(up[n])
        new.append(down[n])
    if len(up)>len(down):
        new.append(up[-1])
    elif len(up)<len(down):
        new.append(down[-1])
    print(f'#{t+1}',end=' ')
    print(*new)