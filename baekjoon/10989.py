import sys
N = int(sys.stdin.readline())
count = [0]*10001
for n in range(N):
    num=int(sys.stdin.readline())
    count[num]+=1
for c in range(10001):
    if count[c]>0:
        for i in range(count[c]):
            print(c)
