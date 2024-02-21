def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        result.append(cal[T-1])

for t in range(10):
    N = int(input())
    cal = []
    lines = []
    result = []
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식번호 저장
    right = [0] * (N + 1)  # 부모를 인덱스로 오른쪽자식번호 저장
    par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장
    for n in range(1, N + 1):
        idx, val, *child = input().split()
        cal.append(val)
        while child:
            lines.append(n)
            lines.append(int(child[0]))
            child.remove(child[0])
    for i in range(N - 1):
        p, c = lines[i * 2], lines[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    c = N
    while par[c] != 0:
        c = par[c]
    root = c
    post_order(root)
    answer = []
    while True:
        if not result:
            break
        a = result.pop(0)
        if a in '-+*/':
            if a=='-':
                x = answer.pop()
                y = answer.pop()
                answer.append(y-x)
            elif a=='+':
                x = answer.pop()
                y = answer.pop()
                answer.append(y+x)
            elif a=='*':
                x = answer.pop()
                y = answer.pop()
                answer.append(y*x)
            elif a=='/':
                x = answer.pop()
                y = answer.pop()
                answer.append(y//x)
        else:
            answer.append(int(a))
    print(f'#{t+1} {answer[0]}')