"""
fx = (6+5*(2-8)/2)
"""
top = -1
stack = [0]*100

icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안

fx = '(6+5*(2-8)/2)'
postfix = ''
for tk in fx:
    # 여는 괄호 push, 연산자이고 top원소보다 우선순위 높으면 push,
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        # push
        top+=1
        stack[top]=tk
    # 연산자이고 top원소보다 우선순위 높지 않으면
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
        # top원소의 우선순위 낮을 때까지 계속 pop
        while isp[stack[top]] >= icp[tk]:
            # pop
            top -= 1
            postfix += stack[top+1]
        # push
        top+=1
        stack[top]=tk
    # 닫는 괄호면 여는 괄호를 만날 때까지 계속 pop
    elif tk == ')':
        while stack[top]!='(':
            # pop
            top -= 1
            postfix += stack[top+1]
        top -= 1 # 여는 괄호 버리기
        stack[top+1]
    else:   # 피연산자
        postfix += tk
print(postfix)