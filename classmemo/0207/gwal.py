T = int(input())
for t in range(T):
    case = input()
    stack = [0]*len(case)
    top = -1
    result = 1
    for c in case:
        if c=='(' or c=='{':
            top += 1
            stack[top] = c
        elif c == ')':
            if top==-1 or stack[top]!='(':
                result = 0
                break
            else:
                stack[top]=0
                top-=1
        elif c == '}' :
            if top==-1 or stack[top]!='{':
                result = 0
                break
            else:
                stack[top]=0
                top-=1
    if top!=-1:
        result = 0
    print(f'#{t+1} {result}')