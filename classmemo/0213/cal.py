for t in range(10):
    T = int(input())
    cal = []
    cal_stack = []
    stack = []
    sentense = input()
    for s in sentense:
        if s == '+':
            if stack:
                cal.append(stack.pop())
                stack.append(s)
            else:
                stack.append(s)
        else:
            cal.append(int(s))
    if stack:
        cal.append(stack[-1])
    for c in cal:
        if c == '+':
            a = cal_stack.pop()
            b = cal_stack.pop()
            cal_stack.append(a+b)
        else:
            cal_stack.append(c)
    print(f'#{t+1} {cal_stack.pop()}')
