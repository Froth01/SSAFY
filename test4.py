T = int(input())

for t in range(T-1):
    print(f'{t+1}')
    score = list(map(int,input().split()))
    repeat_list = {}
    for x in range(len(score)-1):   
        for y in range(len(score)-1):            
            if score[x]-score[y]==0:
                repeat_time = int(score.count(score[x]))
                repeat_list[score[x]] = repeat_time
                score = [x for x in score if x != score[x]]
                break
    values = [value for value in repeat_list.values()]
    maxvalue = max(values)
    maxkeys = [key for key, value in repeat_list.items() if value == maxvalue]
    print(f'#{t+1} {max(maxkeys)}')