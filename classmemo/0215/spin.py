T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    num = list(map(int,input().split()))
    for m in range(M):
        num.append(num.pop(0))
    print(f'#{t+1} {num[0]}')