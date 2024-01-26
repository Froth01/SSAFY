N = int(input())
sang = list(map(int,input().split()))
M = int(input())
num = list(map(int,input().split()))
answer = []
for m in num:
    if m in sang:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)