def dfs(weight,sum_val):
    if weight > K:
        return
    elif weight == K


N,K = map(int,input().split())
goods = []
for _ in range(N):
    w,v = map(int,input().split())
    goods.append((w,v))

