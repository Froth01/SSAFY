T = int(input())
for t in range(T):
    case = input()
    stack = [0]*len(case)
    top = -1
    result = 'YES'
    for c in case:
        if c=='(' :
            top += 1
            stack[top] = c
        elif c == ')':
            if top==-1 or stack[top]!='(':
                result = 'NO'
                break
            else:
                stack[top]=0
                top-=1
    if top!=-1:
        result = 'NO'
    print(result)