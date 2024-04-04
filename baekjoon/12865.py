

N,K = map(int,input().split())
# 배낭의 무게를 0~K까지 놓고 경우를 따진다
# 물건의 수
best = [[0]*(K+1) for _ in range(N)]
goods = []
for _ in range(N):
    w,v = map(int,input().split())
    goods.append((w,v))

