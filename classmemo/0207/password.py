for t in range(10):
    N, num = input().split()
    stack = []
    s = 0
    while s<=len(num)-2:
        n = 1
        if num[s]==num[s+1]:
            while True:
                if s-n>0 and s+n+1<len(num) and num[s-n] == num[s+n+1]:
                    stack.append(s-n)
                    stack.append(s+n+1)
                    n+=1
                else:
                    break
            stack.append(s)
            stack.append(s+1)
        s+=1
    print(f'#{t+1}',end=' ')
    for i in range(len(num)):
        if i in stack:
            continue
        else:
            print(num[i],end='')
    print()


