for t in range(10):
    tc = int(input())
    password = list(map(int,input().split()))
    front = 0
    rear = len(password)-1
    while password[rear]!=0:
        for i in range(1,6):
            if password[front]-i<=0:
                password.pop(front)
                password.append(0)
                break
            else:
                password.append(password.pop(front)-i)
    print(f'#{tc}',end=' ')
    print(*password)