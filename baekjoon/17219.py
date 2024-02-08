import sys
input = sys.stdin.readline

N,M = map(int,input().split())
info = {}
for n in range(N):
    password = input().split()
    info[password[0]]=password[1]
for m in range(M):
    print(info[input().strip()])