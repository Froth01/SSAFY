N = int(input())
dot = []
for n in range(N):
    dot.append(tuple(map(int,input().split())))
dot.sort()
for n in dot:
    print(*n)