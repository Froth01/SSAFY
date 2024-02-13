T = int(input())
for t in range(T):
    code = list(input().split())
    stack = []
    result = 'error'
    for c in code:
        if c not in '/*-+.':
            stack.append(int(c))
        elif c == '.':
            if len(stack)!=1:
                result = 'error'
                break
            result = stack.pop()
        else:
            if len(stack)<2:
                result = 'error'
                break
            elif c=='+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c=='/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b//a)
            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
    print(f'#{t+1} {result}')