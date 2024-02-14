import sys
input = sys.stdin.readline

N,M = map(int,input().split())
num = list(map(int,input().split()))
sum_num = [0]*N
for i in range(N):
    for j in range(i+1):
        sum_num[i]+=num[j]
for m in range(M):
    i,j = map(int,input().split())
    print(sum_num[j]-sum_num[i])
