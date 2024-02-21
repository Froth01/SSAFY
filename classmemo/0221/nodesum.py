T = int(input())
for t in range(T):
    N,M,L = map(int,input().split())
    bin_tree = [0]*(N+1)
    for m in range(M):
        node,val = map(int,input().split())
        bin_tree[node]=val
    if N%2==0:
        bin_tree[N//2]=bin_tree[N]
        N-=1
    for i in range(N,1,-2):
        bin_tree[i//2]=bin_tree[i]+bin_tree[i-1]
    print(f'#{t+1} {bin_tree[L]}')