import sys
input=sys.stdin.readline

def fib(x):
    global count
    if x == 0:
        count[0]+=1
        return 0
    elif x == 1:
        count[1]+=1
        return 1
    else:
        return fib(x-2)+fib(x-1)


T = int(input())
for t in range(T):
    count = [0,0]
    N = int(input())
    fib(N)
    print(*count)
