import sys
input = sys.stdin.readline

A,B = map(int,input().split())
C,D = map(int,input().split())
K = int(input())
turn = 0
if B%K==0:
    turn = B//K
else:
    turn = B//K+1
if (turn*B)-((turn-1)*turn//2)*K>=A:
    for n in range(turn):
        if ((n+1)*D)-C>=((n+1)*B)-(n*(n+1)//2)*K:
            print(-1)
            exit()
        elif ((n+1)*B)-(n*(n+1)//2)*K>=A:
            print(n+1)
            exit()
else:
    print(-1)
    exit()