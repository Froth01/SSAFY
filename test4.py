T = int(input())

for t in range(1,T):
    score = list(map(int,input().split()))
    repeat_list = []
    score.sort()
    score.reverse()
    for x in range(len(score)):
        repeat_list.append(score.count(score[x]))
    result = score[repeat_list.index(max(repeat_list))]
    print(f'#{t} {result}')