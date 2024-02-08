import sys
input = sys.stdin.readline

def COLOR(lst,color):
    global area
    for n in range(len(lst[0])):
        

def BLIND(lst):
    pass


N = int(input())
frame = [list(input().rstrip()) for _ in range(N)]
area = []

for i in range(N):
    for j in range(N-1):
        if frame[i][j]!=0:
            if frame[i][j] != frame[i][j+1]:
               area = j+1


