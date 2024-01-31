'''
5
45 15 10 56 23
96 98 99 40 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14
'''
'''
arr = []
N = int(input())
for n in range(N):
    arr.append(list(map(int,input().split())))
'''
N = int(input())
arr = [list(map(int,input().split())) for n in range(N)]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i-1<0 or i+1>N-1 or j-1<0 or j+1>N-1:
            pass
        else:
            abs(arr[i][j]-arr[i+1]

