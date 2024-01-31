import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().split()))
M = int(input())
for m in range(M):
    count = 0
    i,j,k = map(int,input().split())
    for n in num[i-1:j]:
        count+=(n>k)
    print(count)