def func(n1, n2):
    for i in range(0, len(card), 2):
        global result
        play1, play2 = card[i], card[i + 1]
        n1.append(play1)
        n2.append(play2)

        if len(n1) < 3 and len(n2) < 3:
            continue

        for n in range(10):
            if n1.count(n) >= 3:
                result = 1
                return result
            elif n in n1 and n + 1 in n1 and n + 2 in n1:
                result = 1
                return result

        for n in range(10):
            if n2.count(n) >= 3:
                result = 2
                return result
            elif n in n2 and n + 1 in n2 and n + 2 in n2:
                result = 2
                return result
    return result

T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    n1 = []
    n2 = []
    result = 0
    print(f'#{tc} {func(n1,n2)}')