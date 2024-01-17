T = int(input())

for t in range(T):
    count = 0
    start = int(input())
    plus = start 
    source = set(str(start))
    while True:
        count += 1
        source.update(list(str(start)))
        if len(source) == 10:
            print(f'#{t+1} {count*plus}')
            break
        start += plus
#1288.새로운 불면증 치료법