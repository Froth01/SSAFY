def inorder_traverse(T):
    if T:
        inorder_traverse(left[T])
        result.append(T)
        inorder_traverse(right[T])

for t in range(10):
    N = int(input())
    words = []
    lines = []
    result = []
    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식번호 저장
    right = [0] * (N + 1)  # 부모를 인덱스로 오른쪽자식번호 저장
    par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장
    for n in range(1,N+1):
        idx,word,*child  = input().split()
        words.append(word)
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
    print(f'#{t+1}',end=' ')
    inorder_traverse(root)
    for l in result:
        print(words[l-1],end='')
    print()

