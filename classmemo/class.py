T = int(input())
count = 1
for t in range(T):
    start = int(input())
    source=set(str(start))
        while True:
            source.update(list(str(start)))
            count += 1
            start *= 
            if len(source) == 10:
                print(f'#{t+1} {count}')