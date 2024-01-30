import sys
sys.stdin = open('sample_input (3).txt')

T=int(input())
for t in range(T):
    K,N,M = map(int,input().split())
    charge = list(map(int,input().split()))
    charge.append(N)
    charge_cnt = 0
    re_K = K
    for n in range(1,N+1):
        K-=1
        if K<0:
            charge_cnt = 0
            break
        for c in range(len(charge)-1) :
            if n==charge[c] and charge[c+1]-charge[c]>re_K:
                result = 0
                break
            elif n==charge[c] and charge[c+1]-charge[c]<=re_K:
                if charge[c+1]-charge[c]<=K:
                    break
                else:
                    charge_cnt+=1
                    K=re_K
            elif n==N:
                break
    print(f'#{t+1} {charge_cnt}')
