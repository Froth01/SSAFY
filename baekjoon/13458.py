import sys
input = sys.stdin.readline

N = int(input())
frame = list(map(int,input().split()))
B,C = map(int,input().split())
answer = 0
for f in frame:
    if f<=B:
        answer+=1
        continue
    answer+=1
    f-=B
    answer+=f//C
    if f%C!=0:
        answer+=1
print(answer)