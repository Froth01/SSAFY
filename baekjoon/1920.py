import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int,input().split()))
count = {}
for n in N_lst:
    count[str(n)]=1
M = int(input())
M_lst = list(map(int,input().split()))
for m in M_lst:
    try:
        print(count[str(m)])
    except:
        print(0)