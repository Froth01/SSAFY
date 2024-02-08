import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int,input().split()))
count = [0]*(100001)
for n in N_lst:
    count[n]+=1
M = int(input())
M_lst = list(map(int,input().split()))
for m in M_lst:
    if count[m]>0:
        print(1)
    else:
        print(0)