T = int(input())
for t in range(T):
    string = list(input())
    stack = []

    while True:
        cnt = 0
        for s in range(len(string)-1):
            if string[s]==string[s+1]:
                stack.append(string[s])
                string.pop(s)
                stack.append(string[s])
                string.pop(s)
                cnt+=1
                break
        if cnt==0:
            break
    print(f'#{t+1} {len(string)}')


